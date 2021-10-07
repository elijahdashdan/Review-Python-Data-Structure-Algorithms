# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return(fib(n-1)+fib(n-2))

# print(fib(10))

def printFun(test):
 
    if (test < 1):
        print("here1")
        return
    else:
        print("here2")
 
        print(test, end=" ")
        printFun(test-1)  # statement 2
        print("here")
        print(test, end=" ")
        return
 
# Driver Code
test = 3
printFun(test)