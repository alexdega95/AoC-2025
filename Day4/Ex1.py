with open('/mnt/Storage/Uni/Progettini/adventOfCode25/Day4/input.txt', 'r') as file:
    data = file.readlines()

row = 0

for i in range(len(data)):
    data[i] = data[i].strip()

counter = 0
while row < len(data):
    n = 0
    while n < len(data[row]):
        if data[row][n] == '@': 
            tl = 1 if row != 0 and n != 0 and data[row-1][n-1] == '@' else 0
            tc = 1 if row != 0 and data[row-1][n] == '@' else 0
            tr = 1 if row != 0 and n != len(data[row]) - 1 and data[row-1][n+1] == '@' else 0
            l = 1 if n != 0 and data[row][n-1] == '@' else 0
            r = 1 if n != len(data[row]) - 1 and data[row][n+1] == '@' else 0
            bl = 1 if row != len(data) - 1 and n != 0 and data[row+1][n-1] == '@' else 0
            bc = 1 if row != len(data) - 1 and data[row+1][n] == '@' else 0
            br = 1 if row != len(data) - 1 and n != len(data[row]) - 1 and data[row+1][n+1] == '@' else 0
            neigh = tl + tc + tr + l + r + bl + bc + br

            if neigh < 4:
                counter += 1
        n += 1
    row += 1
print(counter)