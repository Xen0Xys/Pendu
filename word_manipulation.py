class WordManipulation():
    def __init__(self):
        pass
    def actualizeWord(self, _word, _character_list):
        final_word = ""
        word_found = True
        for char in _word:
            if char in _character_list:
                final_word += char
            else:
                final_word += "*"
                word_found = False
        return final_word, word_found