accounts = [[1, 2, 3], [3, 20, 1]]
solutions = []
sum = 0

for i in range(0, len(accounts)):
    # print(accounts[i])
    for j in range(0, len(accounts[i])):
        # print(accounts[i][j])
        sum = accounts[i][j] + sum

    solutions.append(sum)
    sum = 0

print("Solutions :", solutions)

# To find richest customer
greatest = 0
for i in range(0, len(solutions)):
    # greatest = nums[i] if nums[i] > nums[i-1] else nums[i-1]
    greatest = solutions[i] if greatest < solutions[i] else greatest

print("Richest customer wealth :", greatest)

# Greatest of all in a list !
# nums = [1, 20, 4, 3]
# greatest = 0

# for i in range(0, len(nums)):
#     # greatest = nums[i] if nums[i] > nums[i-1] else nums[i-1]
#     greatest = nums[i] if greatest < nums[i] else greatest
#     # if greatest < nums[i]:
#     #     greatest = nums[i]
#     # else:
#     #     greatest = greatest

# print("Greatest :", greatest)
