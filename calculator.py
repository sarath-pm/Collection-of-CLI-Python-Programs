# Addition function
def addition ():
    print("Addition")
    n = float(input("Enter the number: "))
    t = 0 
    add = 0
    while n != 0:
        ans = add + n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans,t]

# Subtraction function
def subtraction ():
    print("Subtraction")
    n = float(input("Enter the number: "))
    t = 0 
    sub = 0
    while n != 0:
        ans = sub - n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans,t]

# Multiplication function
def multiplication ():
    print("Multiplication")
    n = float(input("Enter the number: "))
    t = 0 
    mul = 1
    while n != 0:
        ans = mul * n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans,t]

# Average function
def average():
    an = []
    an = addition()
    t = an[1]
    a = an[0]
    ans = a / t
    return [ans,t]

# Get user input and execute the functions
while True:
    list = []
    print(" My first python program!")
    print(" Simple Calculator in python by Malik Umer Farooq")
    print(" Enter 'a' for addition")
    print(" Enter 's' for substraction")
    print(" Enter 'm' for multiplication")
    print(" Enter 'v' for average")
    print(" Enter 'q' for quit")
    user_input = input(" ")
    if user_input != 'q':
        if user_input == 'a':
            list = addition()
            print("Ans = ", list[0], " Total Inputs ",list[1])
        elif user_input == 's':
            list = subtraction()
            print("Ans = ", list[0], " Total Inputs ",list[1])
        elif user_input == 'm':
            list = multiplication()
            print("Ans = ", list[0], " Total Inputs ",list[1])
        elif user_input == 'v':
            list = average()
            print("Ans = ", list[0], " Total Inputs ",list[1])
        else:
            print ("Invalid character...!")
    else:
        break