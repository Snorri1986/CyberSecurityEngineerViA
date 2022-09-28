class Student:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname


    def introduce(self):
        print("My name is {}. My surname is {}".format(self.name,self.surname))