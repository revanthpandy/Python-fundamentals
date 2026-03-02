import random

a = random.randint(1,10)

while True:
    n = int(input("Take a guess 1 to 10:"))
    if(n == a):
        print("Your got it !!")
        break
    elif(n>a):
        print("lesser!")
    elif(n<a):
        print("Higher!!")
