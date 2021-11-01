#How do you reverse a given string in place?
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
  
# How can a given string be reversed using recursion?
#https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/

def reverse(s):
    if len(s) == 0:
        return s
    else:
        print(s[1:],s[0])
        return reverse(s[1:]) + s[0]
  
s = "Geeksforgeeks"
print("HEY",reverse(s))