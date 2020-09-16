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



val1 = int(input("Enter your 1st value : ")) 

val2 = int(input("Enter your 2nd value : "))


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
    print( '\033[31m' + '----------------------------------------------' + '\033[0m')
    print("-Your result is :: " + str(result))
    print('\033[31m' + '-----------------------------------------------' + '\033[0m')


if usrInput == 1 :
    result = add(val1 , val2)
    printMyStyle(result)

if usrInput == 2 :
    result = subtract(val1 , val2)
    printMyStyle(result)

if usrInput == 3 :
    result = multiply(val1 , val2)
    printMyStyle(result)

if usrInput == 4 :
    result = divide(val1 , val2)
    printMyStyle(result)

if usrInput == 5 :
    result = square(val1)
    printMyStyle(result)

if usrInput <= 0:
    print("You selected the wrong opt.")

if usrInput > 5:
    print("You selected the wrong opt.")









