amt = int(input("Enter Your Annual Income :"))
age = int(input("Enter Your Age :"))

if(amt>1000000):
       print("Tax Rate : 30%\nTax Amount : ",(amt*30)/100)

elif(1000000>=amt>500000):
       print("Tax Rate : 20%\nTax Amount : ",(amt*20)/100)

elif(500000>=amt>300000 and age<80):
       print("Tax Rate : 5%\nTax Amount : ",(amt*5)/100)

elif(300000>=amt>250000 and age<60):
       print("Tax Rate : 5%\nTax Amount : ",(amt*5)/100)

else:
       print("Tax Not Applicable")