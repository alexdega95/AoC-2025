import math

with open('input.txt', 'r') as file:
    data = file.readlines()

i = 0
op = None
final = 0
nums = {row : '' for row in range(len(data) - 1)}

while i < len(data[0]):
    void_check = 0

    # Keep track of the operation to do 
    if data[-1][i] != ' ' and data[-1][i] != '\n':
        op = data[-1][i]

    # Keep track of how many void chars are added
    # If they are equal to the number of rows - 1, all figures have been added
    for row in data[:-1]:
        if row[i] == ' ':
            void_check += 1
        nums[data.index(row)] += row[i]

    # When numbers are complete, check which operation to do and append the result
    if void_check == len(data) - 1:
        if op == '+':
            result += sum(int(nums[n]) for n in range(len(data) - 1)) 
        if op == '*':
            result += math.prod([int(nums[n]) for n in range(len(data) - 1)])
        nums = {row : '' for row in range(len(data) - 1)}

    i += 1

if op == '+':
    final += sum(int(nums[n]) for n in range(len(data) - 1)) 
if op == '*':
    final += math.prod([int(nums[n]) for n in range(len(data) - 1)])

print(final)
