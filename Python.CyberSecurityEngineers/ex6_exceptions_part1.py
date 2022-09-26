from NetworkException import Networkerror
# Exception and own exception
a = 10
b = 0
# Predefined exception
try:
    c = a / b
except ZeroDivisionError:
    print("Do not divide by zero")
# My own exception
try:
    raise Networkerror("Bad hostname")
except Networkerror as e:
    print (e.args)