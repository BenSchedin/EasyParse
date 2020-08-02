"""

    Ben Schedin
    EasyParse
    Implementation

"""


class TextParser:
    def __init__(self, file):
        self.string = self.load(file)

    def __str__(self):
        return self.string

    def __len__(self):
        return len(self.string)

    @staticmethod
    def load(file):
        with open(file, "r") as f:
            string = f.read()

        return string

    def count_chars(self):
        char_dict = {}

        for char in self.string:
            if char not in char_dict:
                char_dict[char] = 1
            elif char in char_dict:
                char_dict[char] += 1

        return char_dict

    def count_words(self):
        word_dict = {}

        for word in self.string.split():
            if word not in word_dict:
                word_dict[word] = 1
            elif word in word_dict:
                word_dict[word] += 1

        return word_dict
