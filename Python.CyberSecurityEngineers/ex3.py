#List example
listExample = [100,234,"Denys",7.02]
print("List example",listExample)
# List append
listExample.append(12)
listExample.append("Shabelnyk")
print("List after append",listExample)
# List delete some elements
del listExample[0]
del listExample[4]
print("List after delete",listExample)
# -----------------------------------
# Dictionary example
myDictExample = {
    "name":"Denys",
    "surname":"Shabelnyk",
    "role":"Student",
    "study":"Python for Security Experts"
}
print("Example of Dictionary",myDictExample)
# List of all keys in the dictionary
print("All keys",myDictExample.keys())
# List of all values in the dictionary
print("All keys",myDictExample.values())
# Change value of a key
myDictExample["role"] = "Best student)"
print("Dictionary after changing value of 'role' key",myDictExample)
# ------------------------------------
# Sets example
setExample = {1,2,3,4.6,10,"Some String"}
print("A set example: ",setExample)
# Try to add duplicate value
setExample.add(1)
print("Set after adding duplicate value: ",setExample) # no errors
# Delete an elemeny from set
setExample.remove(10)
setExample.remove("Some String")
# Set after deleting
print("Set after delating: ",setExample)
# ------------------------------------
# Tuple example
myTupleExample = (1,2,67,8,[1,2,3],"Denys")
print("Tuple example: ",myTupleExample)
# Delete an element from the Tuple
# convert to list
myTupleToList = list(myTupleExample)
myTupleToList.remove("Denys")
# back to tuple
myTupleExample = tuple(myTupleToList)
# Tuple after deleting
print("Tuple after delating",myTupleExample)