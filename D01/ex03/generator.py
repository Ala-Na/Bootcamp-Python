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
        random.shuffle(new_text)
    elif option:
        yield "ERROR"
        return
    for i in new_text:
        yield i

text = "Truc bidule machin.Chouette. machin .Chouette"
for word in generator(text, sep=".", option="shuffle"):
    print(word)