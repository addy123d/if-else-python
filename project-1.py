# Basic Calculator
# import os

# os.system("cls")

print(" Quick and Simple Calculator By Your Name ")

for i in range(0, 67):
    print(" -", end="")
print()


condition = "Yes"

while condition == "Yes":

    # Take two numbers as an user input !
    number_1 = float(input("Enter 1st Number : "))
    number_2 = float(input("Enter 2nd Number : "))

    for i in range(0, 67):
        print(" -", end="")
    print()

    # Choose your operator
    print(''' Choose your operator :
    1 - Addition
    2 - Subtraction
    3 - Multiplication
    4 - Division
    ''')

    operator = int(input())

    # Operator selection

    if operator == 1:
        sum = number_1 + number_2
        print(f'Sum of {number_1} and {number_2} is {sum}')
    elif operator == 2:
        if number_1 > number_2:
            difference = number_1 - number_2
        else:
            difference = number_2 - number_1

        print(f'Difference of {number_1} and {number_2} is {difference}')
    elif operator == 3:
        product = number_1 * number_2
        print(f'Product of {number_1} and {number_2} is {product}')
    elif operator == 4:
        if number_2 == 0:
            print(" Zero Exception happened !")
        division = number_1 / number_2
        print(f'Division of {number_1} and {number_2} is {division}')
    else:
        print(f'{operator} is invalid !')

    print("Do you want to continue ? Yes/No")
    condition = input()


print("**************************** The End ****************************************************")
