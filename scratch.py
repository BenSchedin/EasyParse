import re
import easyparse as ep

easy = ep.TextParser("sample text/easy.txt")
print(type(easy))
easy = easy.string
print(type(easy))
print(easy)

pattern = re.compile(r"a")

matches = pattern.finditer(easy)

data = []

for match in matches:
    print(match.span())
    test = match.span()
    text = easy[test[0]:test[1]]
    data.append(text)

print(data)
