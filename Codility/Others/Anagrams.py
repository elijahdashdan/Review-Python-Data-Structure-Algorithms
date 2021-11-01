# How do you check if two strings are anagrams of each other?
# https://www.geeksforgeeks.org/python-sorted-check-two-strings-anagram-not/#:~:text=if%20(Counter(s1)%20%3D,aren't%20anagrams.%22%20)

def check(s1, s2):
     
    # the sorted strings are checked
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")        
         
# driver code 
s1 ="listen"
s2 ="silent"
check(s1, s2)