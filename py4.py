# Check whether the list is a palindrome or not !

# numbers = [2, 1, 1, 2]

# # Check

# for i in range(1, len(numbers)+1):   # i = 1,2,3,4
#     # print(numbers[len(numbers) - i])
#     # print(numbers[i-1])
#     if(numbers[i-1] == numbers[len(numbers) - i]):


# Pallindrome checker
# numbers = [8, 8, 8, 8]
# length = 0
# for number in range(0, len(numbers)):  # number 0,1,2,3
#     if(numbers[number] == numbers[len(numbers)-(number+1)]):
#         length = length + 1


# if(length == len(numbers)):
#     print("This list is a pallindrome !")
# else:
#     print("Not a pallindrome !")


# String

string = "Hello"
# print(len(string))
# print(string[0])

# for i in range(0, len(string)):
#     print(string[i])
#     print("Index :", i)

# Adding all the numbers in the list !

numbers = [1, 2, 3, 4]
sum = 0
for number in numbers:
    sum = number + sum

result = "Sum of all elements in the list : {total:.2f}"
# printf("Sum is %d", sum)

print(result.format(total=sum))
