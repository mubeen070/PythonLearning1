def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x , y):
    return x * y

def divide(x , y):
    res = x / y 
    return round(res , 3)

def square(x):
    return x*x




print("|----------------------------|")
print("|----------------------------|")
print("|      Press 1 to add        |")
print("|    Press 2 to subtract     |")
print("|    Press 3 to multiply     |")
print("|     Press 4 to divide      |")
print("|     Press 5 to square      |")
print("|----------------------------|")
print("|----------------------------|")

usrInput = int(input("Select your option : ")) 




def printMyStyle(result):
    print( '\033[31m' + '-----------------------------------------------' + '\033[0m')
    print("-Your result is :: " + str(result))
    print('\033[31m' + '-----------------------------------------------' + '\033[0m')


def getInput() :
    val1 = int(input("Enter your 1st value : ")) 
    val2 = int(input("Enter your 2nd value : "))
    return [val1, val2]

def getSingleInput() :
    val1 = int(input("Enter your 1st value : "))
    return [val1]


if usrInput == 1 :

    values = getInput()
    result = add(values[0], values[1])
    printMyStyle(result)

if usrInput == 2 :
    values = getInput()
    result = subtract(values[0] , values[1])
    printMyStyle(result)

if usrInput == 3 :
    values = getInput()
    result = multiply(values[0] , values[1])
    printMyStyle(result)

if usrInput == 4 :
    values = getInput()
    result = divide(values[0] , values[1])
    printMyStyle(result)

if usrInput == 5 :
    values = getSingleInput() 
    result = square(values[0])
    printMyStyle(result)

if usrInput <= 0:
    print("You selected the wrong opt.")

if usrInput > 5:
    print("You selected the wrong opt.")