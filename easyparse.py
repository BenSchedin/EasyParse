"""

    Ben Schedin
    EasyParse
    Implementation

"""

import re


class TextParser:
    def __init__(self, file):
        self.string = self.load(file)
        self.iter_index = 0

    def __iter__(self):
        self.iter_index = 0
        return self

    def __next__(self):
        if self.iter_index >= len(self.string):
            self.iter_index = 0
            raise StopIteration
        else:
            current = self.string[self.iter_index]
            self.iter_index += 1
            return current

    def __getitem__(self, index):
        return self.string[index]

    def __str__(self):
        return self.string

    def __len__(self):
        return len(self.string)

    def __add__(self, other):
        return self.string + other.string

    @staticmethod
    def load(file):
        with open(file, "r") as f:
            string = f.read()

        return string

    def write(self, file, data=None):
        with open(file, "w") as f:
            if data is None:
                f.write(self.string)
            elif type(data) is list:
                string = ""
                for item in data:
                    string += "{}\n\n".format(item)
                f.write(string)

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

    def regex_raw(self, expression):
        pattern = re.compile(r"{}".format(expression))

        matches = pattern.finditer(self.string)

        return matches

    def regex_extract(self, expression):
        matches = self.regex_raw(expression)

        data = []

        for match in matches:
            span = match.span()
            text = self.string[span[0]:span[1]]
            data.append(text)

        return data
