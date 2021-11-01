# How do you count a number of vowels and consonants in a given string?

def vowel_count(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return len([i for i in string.lower() if i in vowels])