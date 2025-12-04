with open('input.txt', 'r') as file:
    data = [list(line.strip()) for line in file]

counter = 0
iteration = 0
moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
while iteration < len(data) * len(data[0]):
    row = 0
    accessible = []
    while row < len(data):
        n = 0
        while n < len(data[row]):
            neigh = 0
            if data[row][n] == '@': 
                for pr, pn in moves:
                    check1, check2 = pr + row, pn + n
                    if 0 <= check1 < len(data) and 0 <= check2 < len(data[0]):
                        if data[check1][check2] == '@':
                            neigh += 1
                if neigh < 4:
                    accessible.append([row, n])
                    counter += 1
            n += 1
        row +=1
    if accessible == []:
        break
    for to_remove in accessible:
        data[to_remove[0]][to_remove[1]] = '.'
    iteration += 1
print(counter)