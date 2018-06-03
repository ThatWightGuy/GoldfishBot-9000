import tweepy
import random
from secrets import *

# tweepy documentation (for later)
# http://tweepy.readthedocs.io/en/v3.5.0/index.html

#api = tweepy.API(auth)

class Glubs:
    def __init__(self, api):
        self.api = api

    def punctuation(self):
        return random.choice(['. ', '? ', '! '])

    def isNewSentence(self):
        return random.choice([True, False])

    def glubType(self):
        return random.choice(["glub", "GLUB"])

    def getNumGlubs(self):
        return random.randint(1, 35)

    def generateGlubs(self):
        print("generating glubs...")

        newSentence = False
        numGlubs = self.getNumGlubs()
        glubString = ""

        for glub in range(numGlubs):
            newGlub = self.glubType()

            if newSentence is True or glub == 0:
                newGlub = newGlub.capitalize()

            glubString += newGlub
            newSentence = self.isNewSentence()

            if newSentence is True or glub == (numGlubs - 1):
                glubString += self.punctuation()
            else:
                glubString += " "

        print("glubs generated...")

        return glubString

    def tweetGlub(self):
        self.api.update_status(self.generateGlubs())

class Tweet_Listener(tweepy.StreamListener):
    def on_data(self, data):
        print("Data found. The goldfish will now speak...", data)
        api = tweepy.API(stream.auth)
        glub = Glubs(api)
        glub.tweetGlub()
        return True

    def on_error(self, status_code):
        print(status_code)

if __name__ == '__main__':
    listener = Tweet_Listener()
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    stream = tweepy.Stream(auth, listener)
    stream.filter(follow=['3051167834'])
