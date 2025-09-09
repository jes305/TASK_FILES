# palindromee
def ispalindrome(s):
    rev=(s[::-1])
    if  rev==s:
        return 0
    return 1
stri=input("enter the string")
pal=ispalindrome(stri)
if pal==0:
    print(stri,'is palindrome')
else:

    print(stri,'not ispalindrome')
