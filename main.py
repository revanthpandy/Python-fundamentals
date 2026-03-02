def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if(b==0):
        return "Error Dividing by Zero"
    return a/b

while True:
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter a choice"))
    
    if(choice == 5):
        break

    a = int(input("Enter a first Number: "))
    b = int(input("Enter a Second Number: "))

    if(choice == 1):
        print(add(a,b))
    elif(choice == 2):
        print(sub(a,b))
    elif(choice == 3):
        print(mul(a,b))
    elif(choice == 4):
        print(div(a,b))
    else:
        print("Enter a valid choice")



