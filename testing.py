"""

    Ben Schedin
    EasyParse
    Test Drivers

"""

import easyparse as ep


def main():
    easy = ep.TextParser("sample text/easy.txt")

    print(easy)
    print(len(easy))


if __name__ == "__main__":
    main()
