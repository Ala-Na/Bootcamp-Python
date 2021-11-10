import random

def generator(text, sep=".", option=None):
    if not isinstance(text, str):
        yield "ERROR"
        return
    new_text = text.split(sep)
    if (option == 'ordered'):
        new_text.sort()
    elif (option == 'unique'):
        new_text = list(dict.fromkeys(new_text))
    elif (option == 'shuffle'):
        i = 0
        while i < len(new_text):
            j = random.randint(0, len(new_text) - 1)
            k = random.randint(0, len(new_text) - 1)
            new_text[j], new_text[k] = new_text[k], new_text[j]
            i += 1
    elif option:
        yield "ERROR"
        return
    for i in new_text:
        yield i

text = "Truc bidule machin.Chouette. machin .Chouette"
for word in generator(text, sep=".", option="shuffle"):
    print(word)