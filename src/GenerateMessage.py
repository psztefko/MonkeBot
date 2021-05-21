from random import randrange
import re

control_number = 0

class GenerateMessage:

    def __init__(self):


        list_of_sentences = self.split_string()

    def split_string(self):

        # reads text form file
        f = open('text.txt')
        self.text = f.read()

        # cuts text into list of sentences
        sentenceEnd = re.compile('[.!?][\s]{1,2}(?=[A-Z])')
        return sentenceEnd.split(self.text, re.UNICODE)

    def get_sentences(self):
        """Returns random amount of sentences from text"""

        return 'test'

    def get_image(self):
        """Returns source of random monkey image"""

        return 'monke\p (' + str(randrange(1097)) + ').jpg'


