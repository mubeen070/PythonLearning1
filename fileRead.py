#x = open("intro.txt", "r")
#print(x.read())

y = open("intro.txt", "a")

usrInput = input("Add your line: ")
y.write("\n" + usrInput)
y.close()


x = open("intro.txt", "r")
print(x.read())

