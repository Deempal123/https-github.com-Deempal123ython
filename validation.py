import re
"""pattern = '^a...s$'
tstring = 'abyss'
result = re.match(pattern,tstring)
print(result)"""

#pattern = '[a-z,A-Z]{8}'
#password validation
'''password = input("Enter the password :")
flag = 0
if (len(password)<8):
    flag = -1
elif not re.search("[a-z]",password):
    flag = -1
elif not re.search("[A-Z]",password):
    flag = -1
elif not re.search("[0-9]",password):
    flag = -1
elif not re.search("[_@$#%&!]",password):
    flag = -1
elif re.search("\s",password):
    flag = -1
else:
    flag = 0
    print("valid Password")

if flag == -1:
    print("Not a Valid Password")'''

#email validation

'''email = input("Enter your Email address :")
pattern = "^[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
result = re.match(pattern,email)
if(result):
    print("Valid Email")
else:
    print("Invalid Email")'''

#name validation
'''name = input("Enter The Name : ")
pattern = "^[A-Za-z]{2,25}\s[A-Za-z]{2,25}$"
result = re.match(pattern,name)
if result:
    print("valid name")
else:
    print("Invalid name")'''

#contact validation
con = input("Enter Contact Number : ")
#pattern = "(?:\+\d{1,3})?\d{3,4}\D?\d{3}\D?\d{3}"
#pattern = "(0|91)?[6-9][0-9]{9}"
pattern = "(0|91)?[6-9][0-9]{9}"
result = re.match(pattern,con)
if result:
    print("Valid Contact Number")
else:
    print("Invalid Contact Number")

    