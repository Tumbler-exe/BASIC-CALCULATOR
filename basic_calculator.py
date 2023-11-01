print("-Basic Calculator-\n")

def addNumber(fNumber,sNumber):
    addResult = fNumber + sNumber
    return addResult

def delNumber(fNumber,sNumber):
    delResult = fNumber - sNumber
    return delResult

def proNumber(fNumber,sNumber):
    proResult = fNumber * sNumber
    return proResult

def divNumber(fNumber,sNumber):
    divResult = fNumber / sNumber
    return divResult


menu = ("""

-Process-

Sum : +
Del : -
Pro : *
Div : /

""")



while True:

    firstNumber = input("\nPlease enter ur first number: ")
    int_firstNumber = int(firstNumber)
    secondNumber = input("Please enter ur second number: ")
    int_secondNumber = int(secondNumber)
    print(menu)
    process = input("Please enter ur process: ")

    if process == "+":
        result = addNumber(int_firstNumber,int_secondNumber)
        print(result)


    elif process == "-":
        result = delNumber(int_firstNumber,int_secondNumber)
        print(result)

    elif process == "*":
        result = proNumber(int_firstNumber,int_secondNumber)
        print(result)

    elif process == "/":
        result = divNumber(int_firstNumber,int_secondNumber)
        print(result)

    else:
        print("Error!")

    input("Press ENTER to return main menu ! ")





