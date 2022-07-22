import string
import sys

def text_analyzer(text = None, *args):
    '''This function counts the number of upper characters, lower characters, punctuation and spaces in a given text.'''
    for elem in args:
        print("ERROR")
        return
    if not text:
        print("What is the text to analyse?")
        text = input(">> ")
    elif type(text) != str:
        print("ERROR")
        return
    nbr_char = 0
    upper_cases = 0
    lower_cases = 0
    punctuations = 0
    spaces = 0
    for element in text:
        if element.isupper():
            upper_cases += 1
        elif element.islower():
            lower_cases += 1
        elif element in string.punctuation:
            punctuations += 1
        elif element in string.whitespace:
            spaces+= 1
        nbr_char += 1
    print("The text contains ", nbr_char, " characters:")
    print("- ", upper_cases, "upper letters")
    print("- ", lower_cases, "lower letters")
    print("- ", punctuations, "punctuation marks")
    print("- ", spaces, "spaces")

if __name__ == '__main__':
    argc = len(sys.argv)
    if (argc < 2):
        text_analyzer()
        exit()
    elif (argc > 2):
        print("ERROR")
        exit()
    text_analyzer(sys.argv[1])
