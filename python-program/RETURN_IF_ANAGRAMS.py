# function to strings and return tue if they are anagrams
def angrams(str1,str2):
    return print (sorted(str1.lower())==sorted (str2.lower()))
angrams("hello","HELLO")
