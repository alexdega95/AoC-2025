import math

with open('input.txt', 'r') as file:
    data = file.readlines()
    for row in data:
        row = row.strip('\n')

i = -2
op = None
final = 0
n = 0
nums = {}
print(len(data[0]))
while abs(i) < len(data[0]) + 1:
    void_check = 0
    nums[n] = ''

    if data[-1][i] != ' ':
        op = data[-1][i]
    
    for row in data[:-1]:
        if row[i] == ' ':
            void_check += 1
        nums[n] += row[i]
    n += 1

    if void_check == len(data) - 1:
        del nums[n-1]
        if op == '+':
            result += sum(int(n) for n in list(nums.values()))
        if op == '*': 
            result += math.prod([int(n) for n in list(nums.values())])
        nums = {}
        n = 0
    i -= 1 

if op == '+':
        final += sum(int(n) for n in list(nums.values()))
if op == '*': 
    final += math.prod([int(n) for n in list(nums.values())])

print(final)
