# Take users input
# user_input = input("Enter a string :")

# # Counting number of characters !
# print(f'User has entered {len(user_input)} characters !')

# # Counting number of words

# print("User input :", user_input)
# words = user_input.split(" ")
# print("Words :", words)

# print(f'User has entered {len(words)} in a string !')

# Expected Output - ['Have' , 'a' , 'nice' , 'day']


# Converting list to string

# string_1 = "10"
# string_2 = "10"

# result = string_1 + string_2

# print(result)

# char_list = ['A', 'D', 'I', 'T', 'Y', 'A']
# empty_string = ""

# for char in char_list:
#     empty_string = empty_string + char

# print(f'My name is {empty_string}')

# Expected Output - 'abcd'


# Indexing

# string = "hello"

# # sub_string = string[-5:-2]
# # print(sub_string)

# for index in range(0, len(string)):
#     print(string[index])

# string[smallnumber : bignumber]


string = "malayalam"

# Expected output - 'Hlo'
print(
    "Pallindrome !") if string == string[::-1] else print("Not a Pallindrome")
