import sys

def checkInt(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def doSum(int_a, int_b):
    res = int_a + int_b
    print('{:10}'.format('Sum:'), res)

def doDiff(int_a, int_b):
    res = int_a - int_b
    print('{:10}'.format('Difference:'), res)

def doProduct(int_a, int_b):
    res = int_a * int_b
    print('{:10}'.format('Product:'), res)

def doQuotient(int_a, int_b):
    if (int_b == 0):
        print('{:10}'.format('Quotient:'), "ERROR (div by zero)")
        return
    res = int_a / int_b
    print('{:10}'.format('Quotient:'), res)

def doModulo(int_a, int_b):
    if (int_b == 0):
        print('{:10}'.format('Remainder:'), "ERROR (modulo by zero)")
        return
    res = int_a % int_b
    print('{:10}'.format('Remainder:'), res)

def doOperations(str_a, str_b):
    if (not checkInt(str_a) or not checkInt(str_b)):
        print("InputError: only integers\n")
        usageMessage()
        return
    int_a = (int)(str_a, 10)
    int_b = (int)(str_b, 10)
    doSum(int_a, int_b)
    doDiff(int_a, int_b)
    doProduct(int_a, int_b)
    doQuotient(int_a, int_b)
    doModulo(int_a, int_b)

def usageMessage():
    print("Usage python operations.py <number1> <number2>")
    print("Example:")
    print("\tpython operations.py 10 3")

argc = len(sys.argv)
if (argc == 1):
    usageMessage()
elif (argc == 2):
    print("InputError: not enough arguments\n")
    usageMessage()
elif (argc > 3):
    print("InputError: too many arguments\n")
    usageMessage()
else:
    doOperations(sys.argv[1], sys.argv[2])
