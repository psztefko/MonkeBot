import numpy as np
import re


class GenerateMessage:

    control_number = 0
    list_of_sentences = None

    def __init__(self):

        self.list_of_sentences = self.split_string()


    def split_string(self):

        # reads text from file
        f = open('text.txt')
        self.text = f.read()

        # cuts text into list of sentences
        sentenceEnd = re.compile('[.!?][\s]{1,2}(?=[A-Z])')
        return sentenceEnd.split(self.text, re.UNICODE)

    def get_sentences(self):
        """Returns random amount of sentences from text"""

        output = ''

        # randomizes the number of sentences with given probabilities
        number_of_sentences = np.random.choice(np.arange(2, 5), p=[0.3, 0.4, 0.3])

        # checks if there are enough sentences in list and if not takes all that's left
        if self.control_number + number_of_sentences > len(self.list_of_sentences):
            number_of_sentences = len(self.list_of_sentences) - self.control_number

        # iterates thought given amount of sentences and concatenates them
        for i in range(self.control_number, self.control_number + number_of_sentences):
            output += self.list_of_sentences[i] + '. '

        self.control_number += number_of_sentences

        return output

    def get_image(self):
        """Returns source of random monkey image"""

        return 'monke\p (' + str(np.random.choice(990)) + ').jpg'


