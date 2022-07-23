import sys
import string

def checkInt(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def checkString(string):
    if isinstance(string, str):
        return True
    return False

def filterWords(words, size):
    while True:
        for element in words:
            if (len(element) <= size):
                words.remove(element)
        if (not words or element == words[-1]):
            break
    return words

argc = len(sys.argv)
if (argc != 3 or not checkString(sys.argv[1]) or not checkInt(sys.argv[2])):
    print("ERROR")
    sys.exit()
text = (sys.argv[1]).translate(str.maketrans('', '', string.punctuation))
list_words = text.split()
res = filterWords(list_words, (int)(sys.argv[2]))
if not res:
    print("[]")
else:
    print(res)
