"""

    Ben Schedin
    EasyParse
    Test Drivers

"""

import easyparse as ep


def main():
    easy = ep.TextParser("sample text/easy.txt")
    medium = ep.TextParser("sample text/medium.txt")

    print(easy)
    print(len(easy))
    print(easy + medium)
    print(easy.count_chars())
    print(easy.count_words())
    print("")

    matches = easy.regex_raw("a")

    for match in matches:
        print(match)

    print(easy.regex_extract("is"))


if __name__ == "__main__":
    main()
