import tweepy
import random
from secrets import *

# tweepy documentation (for later)
# http://tweepy.readthedocs.io/en/v3.5.0/index.html

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

class Glubs:
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

def main():
    glubs = Glubs()

    # api.update_status(glubs.generateGlubs())

if __name__ == '__main__':
    main()