from word_finder import WordFinder
from word_manipulation import WordManipulation

class Main():
    def __init__(self):
        self.word_finder = WordFinder()
        self.word_finder.loadWordList()
        self.secret_word = self.word_finder.wordDraft()
        self.word_manipulation = WordManipulation()
        self.char_list = []
        self.mainLoop()
    def mainLoop(self):
        continue_game = self.word_manipulation.actualizeWord(self.secret_word, self.char_list)[1]
        print(self.secret_word)
        vies = 5
        while continue_game == False and vies > 0:
            char = input("Entrez une lettre: ")
            if len(char) == 1:
                if char not in self.char_list:
                    self.char_list.append(char)
                actually_word, continue_game = self.word_manipulation.actualizeWord(self.secret_word, self.char_list)
                print(actually_word)
                if continue_game == False:
                    vies -= 1
            else:
                pass
        if vies > 0:
            print("Vous avez gagne!!!")
        else:
            print("Vous etes pendu :p")


if __name__ == "__main__":
    Main()