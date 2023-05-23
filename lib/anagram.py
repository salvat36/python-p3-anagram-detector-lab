class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, words):
        return [el for el in words if sorted(self.word) == sorted(el)]