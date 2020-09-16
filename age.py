age = input("Enter your age : ")

age1 = int(age)




def AgeCalculator(age1):
    if age1  <=  16 and age1 > 0 : 
        print( "You are kid." )

    if age1  >  16 and age1 <= 60: 
        print( "You are young." )

    if age1  >  60  and age1 <= 100: 
        print( "You are old." )

    if age1 > 100 or age1 ==  0 or age1 < 0 : 
        print( "Sorry! You entered wrong age." )

    


AgeCalculator(age1)