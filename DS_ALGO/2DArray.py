T = [[11,12,5,2],[15,6,10],[10,8,12,5],[12,15,8,6]]
print(T)

#Accessing
print(T[0])
print(T[0][2])

#Inserting
T.insert(2,[2,3,4,5])
print(T)

#Updating
T[0][3] = 5
print(T)

#Deleting
del T[3][1]
print(T)
