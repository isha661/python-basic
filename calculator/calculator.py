# 
def add (a, b):
    return a+b

def subtract (a, b):
    return a-b

def multiply (a,b):
    return a*b


while True:
    print("\n Calculator")
    print("1. Add")
    print("2. Subtrcat")
    print("3. Multiply")
    print("4. Exit")

    choice = input("choose : ")

    if choice == "4":

        break

    num1 = float(input ("Enter the first number : "))
    num2 = float(input("Enter the second number : "))


    if choice == "1":
        print("Result :", add(num1 ,num2))

    elif choice == "2":
        print("Result :", subtract(num1, num2))

    elif choice == "3":
        print("Result :", multiply(num1, num2))

