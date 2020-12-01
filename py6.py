# numbers = [2, 6, 8, 4, 10, 12]
# resultant_list = []
# # Expected list - [2,6,4,10,12]

# for number in numbers:
#     if number == 8:
#         continue
#     else:
#         resultant_list.append(number)

# print(f'List : {resultant_list}')


numbers = [3, 5, 6, 2, 9, 4]
sum = int(input("Enter"))
number_pairs = []

for index in range(1, len(numbers)):
    total = numbers[index-1] + numbers[index]

    # Compare sum with total
    if sum == total:
        ele = [numbers[index-1], numbers[index]]
        number_pairs.append(ele)

if len(number_pairs) == 0:
    print("Total doesn't match with any pair !")
else:
    print(f'Pairs : {number_pairs}')
