from math import ceil,floor 
s=input("Enter any Number : ")


def pallindrome(s):
        if s==s[::-1]:
               print(s)
        else:
            t=s[:math.ceil(len(s)/2)]
            print(t,end="",s[:len(s)//2]) 
    
pallindrome(s)           