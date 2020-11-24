# if-elif-else statement

# a = 5
# b = 5

# Shorthand method
# print("A equals to b") if a==b else print("oops !")

# Check a is greater than b

# Normal method
# if a > b:
#     print("Yes....a is greater than b")
# elif a == b:
#     print("A is equals to b")
# else:
#     print("Ooops !")


# Calculate student performance based on his/her marks

# Intialise variables
name = input("Enter your name")
first_subject = int(input("Enter Marks of first subject :"))
second_subject = int(input("Enter Marks of second subject :"))
third_subject = int(input("Enter Marks of third subject :"))
fourth_subject = int(input("Enter Marks of fourth subject :"))

# Validate the inputs

if first_subject <= 100 and second_subject <= 100 and third_subject <= 100 and fourth_subject <= 100:

    # Formula
    total = first_subject + second_subject + third_subject + fourth_subject
    percentage = (total/400) * 100

    # Print total marks and percentage
    print("Total Marks of" + " " + name + "is", total)
    print("Percentage of" + " " + name + "is", percentage)

    # Remarks
    # 1. Excellent - 80 above
    # 2. Very Good - 70 and 80
    # 3. Good - 50 and 70
    # 4. Needs to improve - 0 and 50

    if percentage > 80:
        print("Excellent" + " " + name)
    elif percentage >= 70 and percentage <= 80:
        print("Very Good" + " " + name)
    elif percentage >= 50 and percentage < 70:
        print("Good" + " " + name)
    else:
        print("Needs to improve !" + " " + name)


else:
    print("You have entered something wrong !")
