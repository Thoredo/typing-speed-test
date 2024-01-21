import random


class WordGenerator:
    """
    A class for generating random words from a list of common English words.

    Attributes
    ----------
    word_list(list): A list containing common English words.
    """

    def __init__(self):
        """
        Initializes the WordGenerator class by loading common English words and adding an initial word.
        """
        self.word_list = []
        with open("data/common-english-words.txt") as file:
            raw_words = file.readlines()
            for word in raw_words:
                new_word = word.replace("\n", "")
                self.word_list.append(new_word)

    def add_word(self):
        """
        Generates a random word from the word_list.

        Returns
        -------
        randon_word(str): A random word chosen from the common English words list.
        """
        random_word = random.choice(self.word_list)
        return random_word
