import random

class Animals:
    def __init__(self, aName, weight):
        self.aName = aName
        self.weight = weight

    zooName = "Lahore Zoo"

    def age(self):
        return random.randrange(12, 50)
        
    def getFeedTime(self, ft):
        feedTime = ''

        if ft  == "Lion":
            feedTime = "10:00 AM"

        elif ft == "Horse" :
            feedTime = "11:00 AM"

        elif ft == "Zebra" :
            feedTime = "3:00 PM"

        else :
            feedTime = "5:000 PM"

        return feedTime 


animal1 = Animals("Lion",  "200kg" )
animal2 = Animals("Horse", "150kg")
animal3 = Animals("Tiger", "240kg" )    
animal4 = Animals("Giraffe","110kg")
animal5 = Animals("Zebra", "90kg")

zooAnimals = [animal1, animal2, animal3, animal4, animal5]


for x in zooAnimals:
    print("|_______________________________________________________________________________________________")
   # print("Name of animals:" + " " + x.aName + "  " + x.getFeedTime( x.aName ) + " " + "Weight: "+ x.weight +"  "+ "Age:" + str(x.age()))
    print("Name of animals: {} , Feedtime : {} . Zoo Name : {}".format(x.aName,  x.getFeedTime( x.aName ), x.zooName) )
    print("|_______________________________________________________________________________________________")