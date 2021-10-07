from array import *

myArray = array("i", [10,20,30,40,50])

#Access
print(myArray[1])

#Insert
myArray.insert(1,60)
print(myArray)

#Delete
myArray.remove(40)
print(myArray)

#Search
print(myArray.index(50))