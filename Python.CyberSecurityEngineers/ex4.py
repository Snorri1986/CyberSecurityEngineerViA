# While loop
start = 1
end = 10
i = 0
while i <= end:
    print(i)
    i = i+1
    if i == 2:
        print("This %d value is passed",i)
        i = i+1
# else block 
print("The range is over")    
# ---------------------------------------
# For loop in foreach style
myLoopingList = [34,67,89,21]
for s in myLoopingList:
    print(s)
# -------------------------------------
# Looping range
print("Range:")
for x in range(100,135):
    print(x)