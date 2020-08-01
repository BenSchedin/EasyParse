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
