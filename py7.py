# # list declare
# list_1 = [1, 2, 2, 4, 5, 6]

# # Tuple declare
# # tuple_1 = (1, 2, 3, 4, 5, 6)

# # # # Iterate over list
# # # for number in list_1:
# # #     print("List :", number)

# # # # Iterate over tuple
# # # for number in tuple_1:
# # #     print("Tuple :", number)

# # print(dir(list_1))

# list_1.append(10)

# tuple_1 = tuple(list_1)
# print(tuple_1)

# print(tuple_1.count(2))


integer_tuple = (1,)

# Check occurence of every element !
# for integer in integer_tuple:
#     # print(integer)
#     # Check
#     print(f'{integer} occured {integer_tuple.count(integer)} times !')

#     percentage = (integer_tuple.count(integer)/len(integer_tuple))*100
#     if(percentage > 25):
#         print(f'{integer} has occured more than 25%')
#         break

percentage = 44.1111111
integer = 1
str_1 = f'{integer} has occured {percent: .2f}%'
print(str_1.format(percent=percentage))
