import math

expenses = {"January":2200,
"February":2350,
"March":2600,
"April":2130,
"May":2190}

"""1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this"""

#1
print(expenses["February"]-expenses["January"])

#2
Sum = 0
for index, value in enumerate(expenses):
    if index==3:
        break
    else:
        Sum = Sum + int(expenses[value])
print(Sum)

#3
for index, value in enumerate(expenses):
    if int(expenses[value]) ==2000:
        print("YES")

#4
expenses["June"] = 1980
print(expenses)

#5
expenses["April"] = expenses["April"] - 200
print(expenses)