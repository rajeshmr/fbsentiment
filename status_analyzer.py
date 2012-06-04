import data.db as db
import os,re
from classifier.bayes import BayesianClassifier
from datetime import datetime
import operator







FB_DATE_FORMAT = '%Y-%m-%dT%H:%M:%S+0000'
DATE_FORMAT = '%Y-%m-%d'

stop_words = ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already",
 "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", 
 "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", 
 "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", 
 "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", 
 "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", 
 "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", 
 "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", 
 "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", 
 "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", 
 "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", 
 "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", 
 "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", 
 "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", 
 "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", 
 "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", 
 "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", 
 "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", 
 "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", 
 "yours", "yourself", "yourselves", "the", "http", "like"]

class StatusAnalyzer:
	def classify(self, results):
		c = BayesianClassifier()
		c.train(db.fetch_all_status())
		for result in results:
			message = "%s" % result.get('message')
			comments = result.get('comments')
			tag = c.classify(message)
			x = {str('sentiment'):str(tag)}
			result.update(x)
		
			if 'data' in comments:
				for cm in comments.get('data'):
					comment = "%s" % cm.get('message')
					c_tag = c.classify(comment)
					cm.update(sentiment=c_tag)
		return results
		
	def aggregate(self, classified_results):
		
		stats = {BayesianClassifier.POSITIVE: 0, BayesianClassifier.NEGATIVE: 0, BayesianClassifier.NEUTRAL: 0}
		agg = {}
		for result in classified_results:
		  date = datetime.strptime(result['created_time'], FB_DATE_FORMAT)
		  date_str = date.strftime(DATE_FORMAT)
		  if agg.get(date_str) is None:
			agg[date_str] = {BayesianClassifier.POSITIVE: 0, BayesianClassifier.NEGATIVE: 0, BayesianClassifier.NEUTRAL: 0, 'date': date_str}
		  tag = result.get('sentiment') or BayesianClassifier.NEUTRAL
		  agg[date_str][tag] += 1
		  stats[tag] += 1

		# Put the aggregate results in a list and sort them
		agg_list = []
		for i in agg:
		  agg_list.append(agg[i])
		agg_list.sort(cmp=lambda x,y: cmp(x['date'], y['date']))
		return (stats, agg_list)

		classified = {"results": results, "stats": stats}

	@staticmethod
	def genTags(tags):
	    words = {}
	    clou=" "
	    for tag in tags:
			for x in tag.split():
			   if not x in stop_words and len(x)>=4:
				words[x] = 1 + words.get(x, 0)
	    for (x,p) in words.items():
	    	if min(1+p*5/max(words.values()), 5) >= 2:
	    		clou += '<font size="%d"> %s</font>'%(min(1+p*5/max(words.values()), 5), x)
	    return str(clou)
#    	    return ' '.join([('<font size="%d">%s</font>'%(min(1+p*5/max(words.values()), 5), x)) for (x, p) in words.items()])

	@staticmethod
	def genRecentUsers(results):
		users = []
		for result in results:
			post_user = result.get('from')
			post_user_id = post_user.get('id')
			if not post_user_id in users:
				users.append(post_user_id)
			comments = result.get('comments')
			likes = result.get('likes')
			if 'data' in comments:
				for cm in comments.get('data'):
					comment_user = cm.get('from')
					comment_user_id = comment_user.get('id')
					if not comment_user_id in users:
						users.append(comment_user_id)
			if likes:
				for lk in likes.get('data'):
					like_user_id = lk.get('id')
					if not like_user_id in users:
						users.append(like_user_id)
		return users
		
#	def getChar(results):
		
		
		
		
		
		
		

