#define Person class
class Person:
    def __init__(self,name,surname,age,race):
	"This method works like a constructor and builds an object"
        self.name = name
        self.surname = surname
        self.age = age
        self.race = race

 #Getters
    def getName(self):
        return self.name

    def getSurname(self):
        return self.surname

    def getAge(self):
        return self.age

    def getRace(self):
        return self.race

#Setters
    def setName(self,newName):
        self.name = newName

    def setSurname(self,newSurname):
        self.surname = newSurname

    def setAge(self,newAge):
        self.age = newAge
# Person in action
man = Person("Denys","Shabelnyk",36,"White")
woman = Person("Lucy","Ivanova",31,"White")
# Change ages 
setManAge = man.setAge(input("Enter age of a man:"))
setWomanAge = woman.setAge(input("Enter age of a woman:"))
manAge = int(man.getAge())
womanAge = int(woman.getAge())
if (manAge or womanAge) > 30:
    print("We are adult")
elif (manAge or womanAge) < 18:
    print("We are teenagers")
else:
    print("Midlle ages")