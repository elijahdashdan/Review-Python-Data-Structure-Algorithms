# How do you convert a given String into int like the atoi()

def myAtoi(string):
    res = 0
 
    # Iterate through all characters of
    #  input string and update result
    for i in xrange(len(string)):
        res = res * 10 + (ord(string[i]) - ord('0'))
 
    return res
 
 
# Driver program
string = "89789"
 
# Function call
print myAtoi(string)
 