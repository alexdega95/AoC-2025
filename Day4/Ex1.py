with open('input.txt', 'r') as file:
    data = file.readlines()

row = 0

for i in range(len(data)):
    data[i] = data[i].strip()

rel_pos = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] 

counter = 0
while row < len(data):
    n = 0
    while n < len(data[row]):
        if data[row][n] == '@':
            neigh = 0
            for pr, pn in rel_pos:
                check1, check2 = pr + row, pn + n
                if 0 <= check1 < len(data) and 0 <= check2 < len(data[0]):
                    if data[check1][check2] == '@':
                        neigh += 1
            if neigh < 4:
                counter += 1
        n += 1
    row += 1
print(counter)