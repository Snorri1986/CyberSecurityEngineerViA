# define Car class
from contextlib import redirect_stderr

class Car:
    def __init__(self,color,power,type,price):
	"This method works like a constructor and builds an object"
        self.color = color
        self.power = power
        self.type = type
        self.price = price
# Getters
    def getColor(self):
        return self.color

    def getPower(self):
        return self.power

    def getType(self):
        return self.type

    def getPrice(self):
        return self.price

    def run(self):
        print("Car is driving now")

    def stop(self):
        print("Car is stoping now")

# Setters
    def setColor(self,newColor):
        self.color = newColor 
        
    def setPower(self,newPower):
        self.power = newPower

    def setPrice(self,newPrice):
        self.price = newPrice

# Car in action
vehicle = Car("black",1000,"sedan",23000)
speed = input("Enter current speed")
if int(speed) > 0:
    vehicle.run()
elif int(speed) == 0:
    vehicle.stop()   
else:
    print("Unknown state")     
# Change color of a car
color = "red"
vehicle.setColor(color)
#Show result
print("New car color is ",vehicle.getColor())