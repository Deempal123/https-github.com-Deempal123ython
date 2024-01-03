import re 
t=False
f=open('file.txt','r')
s=input('Enter a String To search: ')
for l in f:
    if re.search(s, l):
        t=True
        break
	
if t:
    print("It is In the File") 
else:
    print('Sorry String Not found ')
