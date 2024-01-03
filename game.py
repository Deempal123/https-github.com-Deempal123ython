import random

money=0
turns=int(input("Enter how many times to play "))

def check(n,guess):
      if n == guess:
           return 100
      elif n[0] in guess or n[1] in guess:
           return 10
      else:
           return 0

while turns:
      n=str(random.randint(1,99))
      guess=input("Guess a Number ")
      money=money+check(n,guess)
      print("Number Was ",n)
      print("Your Guess ",guess)
      turns=turns-1
print("You Won! ",money," Rs")    
