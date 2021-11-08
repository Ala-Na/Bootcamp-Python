import sys

Morse_dic = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.'
}

def checkIsAlnum(input):
    if all(char.isalnum() or char.isspace() for char in input):
        return True
    return False

def printMorseMode(word):
    for letter in word:
        if (letter == ' '):
            print(" / ", end='')
        else:
            print("{} ".format(Morse_dic[letter.upper()]), end ='')

argc = len(sys.argv)
index = 1
while (index < argc):
    if not checkIsAlnum(sys.argv[index]):
        print("ERROR")
        sys.exit()
    index += 1
index = 1
while (index < argc):
    printMorseMode(sys.argv[index])
    index += 1
    if (index != argc):
        print(" / ", end='')
    else:
        print("")