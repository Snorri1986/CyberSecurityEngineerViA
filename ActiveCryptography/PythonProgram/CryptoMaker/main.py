from files import encryptfile
from files import decryptfile
print("Welcome")
print("What we are going to done: 1 - encrypt; 2-decrypt")
userchoice = input()
print("You have choiced",userchoice)
userchoiceAsNumber = int(userchoice)
if userchoiceAsNumber == 1 :
    encryptfile()
elif userchoiceAsNumber == 2 :
    decryptfile()
else :
    print("Wrong number. Only 1 or 2 is allowed")

