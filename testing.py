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

    print(easy.iter_index)
    easy.index = 10
    print(easy.iter_index)
    for char in easy:
        print(char)
    print(easy.iter_index)
    print("")

    matches = easy.regex_raw("is")

    for match in matches:
        print(match)
    print("")

    print(easy.regex_extract("is"))
    print("")

    print(easy[1])
    print("")

    string = ""
    for item in easy.regex_extract("is"):
        string += "{}\n\n".format(item)
    print(string)
    print("")

    easy.write("output/test1.txt")
    easy.write("output/test2.txt", data=easy.regex_extract("is"))


if __name__ == "__main__":
    main()
