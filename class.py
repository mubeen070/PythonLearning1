import json

class Course:
    def __init__(self, cName , cFee ):
        self.cName = cName
        self.cFee = cFee

    def getCourses():

        courses = ["Maths", "English"]
        return courses



class Student:
    def __init__(self, sName, fName, email, adress):
        self.sName = sName
        self.fName = fName
        self.email = email
        self.adress = adress

    





def write_json(data, filename='StudentData.json'): 
    with open(filename,'a') as f: 
        json.dump(data, f, indent=4) 


def read_json(filename='StudentData.json'): 
    with open(filename) as f:
        data = json.load(f)
        return data


student1 = Student("dffdsf", "sefrser", "mubeen070@gmahotaill.com", "house#295")


for x in Course.getCourses() :
    print(x) 




#jsonStr = json.dumps(student1.__dict__)

#print(jsonStr)

#write_json(jsonStr)

