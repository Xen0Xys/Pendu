from random import randint

class WordFinder():
    def __init__(self):
        pass
    def loadWordList(self):
        self.word_list = []
        with open("mots.txt", "r") as file:
            ct = file.read()
            for mot in ct.split("\n"):
                self.word_list.append(mot)
        return self.word_list
    def wordDraft(self, word_list=None):
        if word_list == None:
            random = randint(0, len(self.word_list) - 1)
            self.current_word = self.word_list[random]
            return self.current_word
        else:
            random = randint(0, len(word_list) - 1)
            self.current_word = word_list[random]
            return self.current_word