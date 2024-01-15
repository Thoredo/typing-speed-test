import random


class WordGenerator:
    def __init__(self):
        self.word_list = []
        with open("common-english-words.txt") as file:
            raw_words = file.readlines()
            for word in raw_words:
                new_word = word.replace("\n", "")
                self.word_list.append(new_word)

        self.add_word()

    def add_word(self):
        random_word = random.choice(self.word_list)
        return random_word
