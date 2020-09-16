import random

class Student:

    def __init__(self, fName, lName, email, age):
        self.fName = fName
        self.lName = lName
        self.email = email
        self.age = age

    def fullName(self):
        return self.fName + " , " +self.lName

    def getRollNumber(self):
        return random.randrange(200, 2000)


    
    



student1 = Student("Mubeen", "Khalid", "mubeen@gmail.com", 19)
student2 = Student("Hamza", "Imran", "hamza@gmail.com", 18)
student3 = Student("Ahsan", "Ather", "zain@gmail.com", 20)

mathCourseClass = [student1, student2, student3]


for x in mathCourseClass:
  print(  "Student's name and email is :  "  +  x.fullName() +  " , " + x.email + " , " + str(x.age) + str(x.getRollNumber()))



