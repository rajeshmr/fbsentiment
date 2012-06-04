#!/usr/bin/python

from reverend.thomas import Bayes

POSITIVE = "pos"
NEGATIVE = "neg"
NEUTRAL  = "neu"

class BayesianClassifier:

  POSITIVE = POSITIVE
  NEGATIVE = NEGATIVE
  NEUTRAL  = NEUTRAL

  THRESHHOLD = 0.1
  guesser = None

  def __init__(self):
    self.guesser = Bayes()

  def train(self, example_tweets):
    for t in example_tweets:
      self.guesser.train(t.sentiment, t.message)

    self.guesser.train(POSITIVE, "cool")
    self.guesser.train(POSITIVE, "Woo")
    self.guesser.train(POSITIVE, "quite amazing")
    self.guesser.train(POSITIVE, "thks")
    self.guesser.train(POSITIVE, "looking forward to")
    self.guesser.train(POSITIVE, "damn good")
    self.guesser.train(POSITIVE, "frickin ruled")
    self.guesser.train(POSITIVE, "frickin rules")
    self.guesser.train(POSITIVE, "Way to go")
    self.guesser.train(POSITIVE, "cute")
    self.guesser.train(POSITIVE, "comeback")
    self.guesser.train(POSITIVE, "not suck")
    self.guesser.train(POSITIVE, "prop")
    self.guesser.train(POSITIVE, "kinda impressed")
    self.guesser.train(POSITIVE, "props")
    self.guesser.train(POSITIVE, "come on")
    self.guesser.train(POSITIVE, "congratulation")
    self.guesser.train(POSITIVE, "gtd")
    self.guesser.train(POSITIVE, "proud")
    self.guesser.train(POSITIVE, "thanks")
    self.guesser.train(POSITIVE, "can help")
    self.guesser.train(POSITIVE, "thanks!")
    self.guesser.train(POSITIVE, "pumped")
    self.guesser.train(POSITIVE, "integrate")
    self.guesser.train(POSITIVE, "really like")
    self.guesser.train(POSITIVE, "loves it")
    self.guesser.train(POSITIVE, "yay")
    self.guesser.train(POSITIVE, "amazing")
    self.guesser.train(POSITIVE, "epic flail")
    self.guesser.train(POSITIVE, "flail")
    self.guesser.train(POSITIVE, "good luck")
    self.guesser.train(POSITIVE, "fail")
    self.guesser.train(POSITIVE, "life saver")
    self.guesser.train(POSITIVE, "piece of cake")
    self.guesser.train(POSITIVE, "good thing")
    self.guesser.train(POSITIVE, "hawt")
    self.guesser.train(POSITIVE, "hawtness")
    self.guesser.train(POSITIVE, "highly positive")
    self.guesser.train(POSITIVE, "my hero")
    self.guesser.train(POSITIVE, "yummy")
    self.guesser.train(POSITIVE, "awesome")
    self.guesser.train(POSITIVE, "congrats")
    self.guesser.train(POSITIVE, "would recommend")
    self.guesser.train(POSITIVE, "intellectual vigor")
    self.guesser.train(POSITIVE, "really neat")
    self.guesser.train(POSITIVE, "yay")
    self.guesser.train(POSITIVE, "ftw")
    self.guesser.train(POSITIVE, "I want")
    self.guesser.train(POSITIVE, "best looking")
    self.guesser.train(POSITIVE, "imrpessive")
    self.guesser.train(POSITIVE, "positive")
    self.guesser.train(POSITIVE, "thx")
    self.guesser.train(POSITIVE, "thanks")
    self.guesser.train(POSITIVE, "thank you")
    self.guesser.train(POSITIVE, "endorse")
    self.guesser.train(POSITIVE, "clearly superior")
    self.guesser.train(POSITIVE, "superior")
    self.guesser.train(POSITIVE, "really love")
    self.guesser.train(POSITIVE, "woot")
    self.guesser.train(POSITIVE, "w00t")
    self.guesser.train(POSITIVE, "super")
    self.guesser.train(POSITIVE, "wonderful")
    self.guesser.train(POSITIVE, "leaning towards")
    self.guesser.train(POSITIVE, "rally")
    self.guesser.train(POSITIVE, "incredible")
    self.guesser.train(POSITIVE, "the best")
    self.guesser.train(POSITIVE, "is the best")
    self.guesser.train(POSITIVE, "strong")
    self.guesser.train(POSITIVE, "would love")
    self.guesser.train(POSITIVE, "rally")
    self.guesser.train(POSITIVE, "very quickly")
    self.guesser.train(POSITIVE, "very cool")
    self.guesser.train(POSITIVE, "absolutely love")
    self.guesser.train(POSITIVE, "very exceptional")
    self.guesser.train(POSITIVE, "so proud")
    self.guesser.train(POSITIVE, "funny")
    self.guesser.train(POSITIVE, "recommend")
    self.guesser.train(POSITIVE, "so proud")
    self.guesser.train(POSITIVE, "so great")
    self.guesser.train(POSITIVE, "so cool")
    self.guesser.train(POSITIVE, "cool")
    self.guesser.train(POSITIVE, "wowsers")
    self.guesser.train(POSITIVE, "plus")
    self.guesser.train(POSITIVE, "liked it")
    self.guesser.train(POSITIVE, "make a difference")
    self.guesser.train(POSITIVE, "moves me")
    self.guesser.train(POSITIVE, "inspired")
    self.guesser.train(POSITIVE, "OK")
    self.guesser.train(POSITIVE, "love it")
    self.guesser.train(POSITIVE, "LOL")
    self.guesser.train(POSITIVE, ":)")
    self.guesser.train(POSITIVE, ";)")
    self.guesser.train(POSITIVE, ":-)")
    self.guesser.train(POSITIVE, ";-)")
    self.guesser.train(POSITIVE, ":D")
    self.guesser.train(POSITIVE, ";]")
    self.guesser.train(POSITIVE, ":]")
    self.guesser.train(POSITIVE, ":p")
    self.guesser.train(POSITIVE, ";p")
    self.guesser.train(POSITIVE, "voting for")
    self.guesser.train(POSITIVE, "great")
    self.guesser.train(POSITIVE, "agreeable")
    self.guesser.train(POSITIVE, "amused")
    self.guesser.train(POSITIVE, "brave")
    self.guesser.train(POSITIVE, "calm")
    self.guesser.train(POSITIVE, "charming")
    self.guesser.train(POSITIVE, "cheerful")
    self.guesser.train(POSITIVE, "comfortable")
    self.guesser.train(POSITIVE, "cooperative")
    self.guesser.train(POSITIVE, "courageous")
    self.guesser.train(POSITIVE, "delightful")
    self.guesser.train(POSITIVE, "determined")
    self.guesser.train(POSITIVE, "eager")
    self.guesser.train(POSITIVE, "elated")
    self.guesser.train(POSITIVE, "enchanting")
    self.guesser.train(POSITIVE, "encouraging")
    self.guesser.train(POSITIVE, "energetic")
    self.guesser.train(POSITIVE, "enthusiastic")
    self.guesser.train(POSITIVE, "excited")
    self.guesser.train(POSITIVE, "exuberant")
    self.guesser.train(POSITIVE, "excellent")
    self.guesser.train(POSITIVE, "I like")
    self.guesser.train(POSITIVE, "fine")
    self.guesser.train(POSITIVE, "fair")
    self.guesser.train(POSITIVE, "faithful")
    self.guesser.train(POSITIVE, "fantastic")
    self.guesser.train(POSITIVE, "fine")
    self.guesser.train(POSITIVE, "friendly")
    self.guesser.train(POSITIVE, "fun ")
    self.guesser.train(POSITIVE, "funny")
    self.guesser.train(POSITIVE, "gentle")
    self.guesser.train(POSITIVE, "glorious")
    self.guesser.train(POSITIVE, "good")
    self.guesser.train(POSITIVE, "pretty good")
    self.guesser.train(POSITIVE, "happy")
    self.guesser.train(POSITIVE, "healthy")
    self.guesser.train(POSITIVE, "helpful")
    self.guesser.train(POSITIVE, "high")
    self.guesser.train(POSITIVE, "agile")
    self.guesser.train(POSITIVE, "responsive")
    self.guesser.train(POSITIVE, "hilarious")
    self.guesser.train(POSITIVE, "jolly")
    self.guesser.train(POSITIVE, "joyous")
    self.guesser.train(POSITIVE, "kind")
    self.guesser.train(POSITIVE, "lively")
    self.guesser.train(POSITIVE, "lovely")
    self.guesser.train(POSITIVE, "lucky")
    self.guesser.train(POSITIVE, "nice")
    self.guesser.train(POSITIVE, "nicely")
    self.guesser.train(POSITIVE, "obedient")
    self.guesser.train(POSITIVE, "perfect")
    self.guesser.train(POSITIVE, "pleasant")
    self.guesser.train(POSITIVE, "proud")
    self.guesser.train(POSITIVE, "relieved")
    self.guesser.train(POSITIVE, "silly")
    self.guesser.train(POSITIVE, "smiling")
    self.guesser.train(POSITIVE, "splendid")
    self.guesser.train(POSITIVE, "successful")
    self.guesser.train(POSITIVE, "thankful")
    self.guesser.train(POSITIVE, "thoughtful")
    self.guesser.train(POSITIVE, "victorious")
    self.guesser.train(POSITIVE, "vivacious")
    self.guesser.train(POSITIVE, "witty")
    self.guesser.train(POSITIVE, "wonderful")
    self.guesser.train(POSITIVE, "zealous")
    self.guesser.train(POSITIVE, "zany")
    self.guesser.train(POSITIVE, "rocks")
    self.guesser.train(POSITIVE, "comeback")
    self.guesser.train(POSITIVE, "pleasantly surprised")
    self.guesser.train(POSITIVE, "pleasantly")
    self.guesser.train(POSITIVE, "surprised")
    self.guesser.train(POSITIVE, "love")
    self.guesser.train(POSITIVE, "glad")
    self.guesser.train(POSITIVE, "yum")
    self.guesser.train(POSITIVE, "interesting")



    self.guesser.train(NEGATIVE, "FTL")
    self.guesser.train(NEGATIVE, "fuck")
    self.guesser.train(NEGATIVE, "irritating")
    self.guesser.train(NEGATIVE, "not that good")
    self.guesser.train(NEGATIVE, "suck")
    self.guesser.train(NEGATIVE, "lying")
    self.guesser.train(NEGATIVE, "duplicity")
    self.guesser.train(NEGATIVE, "angered")
    self.guesser.train(NEGATIVE, "dumbfounding")
    self.guesser.train(NEGATIVE, "dumbifying")
    self.guesser.train(NEGATIVE, "not as good")
    self.guesser.train(NEGATIVE, "not impressed")
    self.guesser.train(NEGATIVE, "stomach it")
    self.guesser.train(NEGATIVE, "pw")
    self.guesser.train(NEGATIVE, "pwns")
    self.guesser.train(NEGATIVE, "pwnd")
    self.guesser.train(NEGATIVE, "pwning")
    self.guesser.train(NEGATIVE, "in a bad way")
    self.guesser.train(NEGATIVE, "horrifying")
    self.guesser.train(NEGATIVE, "wrong")
    self.guesser.train(NEGATIVE, "flailing")
    self.guesser.train(NEGATIVE, "failing")
    self.guesser.train(NEGATIVE, "fallen way behind")
    self.guesser.train(NEGATIVE, "fallen behind")
    self.guesser.train(NEGATIVE, "lose")
    self.guesser.train(NEGATIVE, "fallen")
    self.guesser.train(NEGATIVE, "self-deprecating")
    self.guesser.train(NEGATIVE, "hunker down")
    self.guesser.train(NEGATIVE, "duh")
    self.guesser.train(NEGATIVE, "get killed by")
    self.guesser.train(NEGATIVE, "got killed by")
    self.guesser.train(NEGATIVE, "hated us")
    self.guesser.train(NEGATIVE, "only works in safari")
    self.guesser.train(NEGATIVE, "must have ie")
    self.guesser.train(NEGATIVE, "fuming and frothing")
    self.guesser.train(NEGATIVE, "heavy")
    self.guesser.train(NEGATIVE, "buggy")
    self.guesser.train(NEGATIVE, "unusable")
    self.guesser.train(NEGATIVE, "nothing is")
    self.guesser.train(NEGATIVE, "is great until")
    self.guesser.train(NEGATIVE, "don't support")
    self.guesser.train(NEGATIVE, "despise")
    self.guesser.train(NEGATIVE, "pos")
    self.guesser.train(NEGATIVE, "hindrance")
    self.guesser.train(NEGATIVE, "sucks")
    self.guesser.train(NEGATIVE, "problems")
    self.guesser.train(NEGATIVE, "not working")
    self.guesser.train(NEGATIVE, "fuming")
    self.guesser.train(NEGATIVE, "annoying")
    self.guesser.train(NEGATIVE, "frothing")
    self.guesser.train(NEGATIVE, "poorly")
    self.guesser.train(NEGATIVE, "headache")
    self.guesser.train(NEGATIVE, "completely wrong")
    self.guesser.train(NEGATIVE, "sad news")
    self.guesser.train(NEGATIVE, "didn't last")
    self.guesser.train(NEGATIVE, "lame")
    self.guesser.train(NEGATIVE, "pet peeves")
    self.guesser.train(NEGATIVE, "pet peeve")
    self.guesser.train(NEGATIVE, "can't send")
    self.guesser.train(NEGATIVE, "bullshit")
    self.guesser.train(NEGATIVE, "fail")
    self.guesser.train(NEGATIVE, "so terrible")
    self.guesser.train(NEGATIVE, "negative")
    self.guesser.train(NEGATIVE, "anooying")
    self.guesser.train(NEGATIVE, "an issue")
    self.guesser.train(NEGATIVE, "drop dead")
    self.guesser.train(NEGATIVE, "trouble")
    self.guesser.train(NEGATIVE, "brainwashed")
    self.guesser.train(NEGATIVE, "smear")
    self.guesser.train(NEGATIVE, "commie")
    self.guesser.train(NEGATIVE, "communist")
    self.guesser.train(NEGATIVE, "anti-women")
    self.guesser.train(NEGATIVE, "WTF")
    self.guesser.train(NEGATIVE, "anxiety")
    self.guesser.train(NEGATIVE, "STING")
    self.guesser.train(NEGATIVE, "nobody spoke")
    self.guesser.train(NEGATIVE, "yell")
    self.guesser.train(NEGATIVE, "Damn")
    self.guesser.train(NEGATIVE, "aren't")
    self.guesser.train(NEGATIVE, "anti")
    self.guesser.train(NEGATIVE, "i hate")
    self.guesser.train(NEGATIVE, "hate")
    self.guesser.train(NEGATIVE, "dissapointing")
    self.guesser.train(NEGATIVE, "doesn't recommend")
    self.guesser.train(NEGATIVE, "the worst")
    self.guesser.train(NEGATIVE, "worst")
    self.guesser.train(NEGATIVE, "expensive")
    self.guesser.train(NEGATIVE, "crap")
    self.guesser.train(NEGATIVE, "socialist")
    self.guesser.train(NEGATIVE, "won't")
    self.guesser.train(NEGATIVE, "wont")
    self.guesser.train(NEGATIVE, ":(")
    self.guesser.train(NEGATIVE, ":-(")
    self.guesser.train(NEGATIVE, "Thanks")
    self.guesser.train(NEGATIVE, "smartass")
    self.guesser.train(NEGATIVE, "don't like")
    self.guesser.train(NEGATIVE, "too bad")
    self.guesser.train(NEGATIVE, "frickin")
    self.guesser.train(NEGATIVE, "snooty")
    self.guesser.train(NEGATIVE, "knee jerk")
    self.guesser.train(NEGATIVE, "jerk")
    self.guesser.train(NEGATIVE, "reactionist")
    self.guesser.train(NEGATIVE, "MUST DIE")
    self.guesser.train(NEGATIVE, "no more")
    self.guesser.train(NEGATIVE, "hypocrisy")
    self.guesser.train(NEGATIVE, "ugly")
    self.guesser.train(NEGATIVE, "too slow")
    self.guesser.train(NEGATIVE, "not reliable")
    self.guesser.train(NEGATIVE, "noise")
    self.guesser.train(NEGATIVE, "crappy")
    self.guesser.train(NEGATIVE, "horrible")
    self.guesser.train(NEGATIVE, "bad quality")
    self.guesser.train(NEGATIVE, "angry")
    self.guesser.train(NEGATIVE, "annoyed")
    self.guesser.train(NEGATIVE, "anxious")
    self.guesser.train(NEGATIVE, "arrogant")
    self.guesser.train(NEGATIVE, "ashamed")
    self.guesser.train(NEGATIVE, "awful")
    self.guesser.train(NEGATIVE, "bad")
    self.guesser.train(NEGATIVE, "bewildered")
    self.guesser.train(NEGATIVE, "blues")
    self.guesser.train(NEGATIVE, "bored")
    self.guesser.train(NEGATIVE, "clumsy")
    self.guesser.train(NEGATIVE, "combative")
    self.guesser.train(NEGATIVE, "condemned")
    self.guesser.train(NEGATIVE, "confused")
    self.guesser.train(NEGATIVE, "crazy")
    self.guesser.train(NEGATIVE, "flipped-out")
    self.guesser.train(NEGATIVE, "creepy")
    self.guesser.train(NEGATIVE, "cruel")
    self.guesser.train(NEGATIVE, "dangerous")
    self.guesser.train(NEGATIVE, "defeated")
    self.guesser.train(NEGATIVE, "defiant")
    self.guesser.train(NEGATIVE, "depressed")
    self.guesser.train(NEGATIVE, "disgusted")
    self.guesser.train(NEGATIVE, "disturbed")
    self.guesser.train(NEGATIVE, "dizzy")
    self.guesser.train(NEGATIVE, "dull")
    self.guesser.train(NEGATIVE, "embarrassed")
    self.guesser.train(NEGATIVE, "envious")
    self.guesser.train(NEGATIVE, "evil")
    self.guesser.train(NEGATIVE, "fierce")
    self.guesser.train(NEGATIVE, "foolish")
    self.guesser.train(NEGATIVE, "frantic")
    self.guesser.train(NEGATIVE, "frightened")
    self.guesser.train(NEGATIVE, "grieving")
    self.guesser.train(NEGATIVE, "grumpy")
    self.guesser.train(NEGATIVE, "helpless")
    self.guesser.train(NEGATIVE, "homeless")
    self.guesser.train(NEGATIVE, "hungry")
    self.guesser.train(NEGATIVE, "hurt")
    self.guesser.train(NEGATIVE, "ill")
    self.guesser.train(NEGATIVE, "itchy")
    self.guesser.train(NEGATIVE, "jealous")
    self.guesser.train(NEGATIVE, "jittery")
    self.guesser.train(NEGATIVE, "lazy")
    self.guesser.train(NEGATIVE, "lonely")
    self.guesser.train(NEGATIVE, "mysterious")
    self.guesser.train(NEGATIVE, "nasty")
    self.guesser.train(NEGATIVE, "rape")
    self.guesser.train(NEGATIVE, "naughty")
    self.guesser.train(NEGATIVE, "nervous")
    self.guesser.train(NEGATIVE, "nutty")
    self.guesser.train(NEGATIVE, "obnoxious")
    self.guesser.train(NEGATIVE, "outrageous")
    self.guesser.train(NEGATIVE, "panicky")
    self.guesser.train(NEGATIVE, "fucking up")
    self.guesser.train(NEGATIVE, "repulsive")
    self.guesser.train(NEGATIVE, "scary")
    self.guesser.train(NEGATIVE, "selfish")
    self.guesser.train(NEGATIVE, "sore")
    self.guesser.train(NEGATIVE, "tense")
    self.guesser.train(NEGATIVE, "terrible")
    self.guesser.train(NEGATIVE, "testy")
    self.guesser.train(NEGATIVE, "thoughtless")
    self.guesser.train(NEGATIVE, "tired")
    self.guesser.train(NEGATIVE, "troubled")
    self.guesser.train(NEGATIVE, "upset")
    self.guesser.train(NEGATIVE, "uptight")
    self.guesser.train(NEGATIVE, "weary")
    self.guesser.train(NEGATIVE, "wicked")
    self.guesser.train(NEGATIVE, "worried")
    self.guesser.train(NEGATIVE, "is a fool")
    self.guesser.train(NEGATIVE, "painful")
    self.guesser.train(NEGATIVE, "pain")
    self.guesser.train(NEGATIVE, "gross")

  def classify(self, sentence):
    guess = self.guesser.guess(sentence)
    if len(guess) == 0:
      return NEUTRAL

    if len(guess) == 1:
      (sentiment, probabitily) = guess[0]
      return sentiment

    (max_sentiment, max_value) = guess[0]
    (min_sentiment, min_value) = guess[1]
    if max_value - min_value > self.THRESHHOLD:
      return max_sentiment

    return NEUTRAL