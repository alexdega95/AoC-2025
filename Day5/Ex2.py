with open('/mnt/Storage/Uni/Progettini/adventOfCode25/Day5/input.txt', 'r') as file:
    data = file.readlines()
to_sort = []
for row in data:
    if row == '\n':
        break
    vals = row.strip().split('-')
    to_sort.append([int(vals[0]), int(vals[1])])
sorted_ranges = sorted(to_sort, key= lambda x: x[1], reverse=True)

counter = 0
range_start = 0
range_end = 0
full_ranges = []
for r in sorted_ranges:
    if r[1] < range_start-1:
        full_ranges.append([range_start, range_end])
        range_start = 0
        range_end = 0
    if range_end == 0:
        range_start = r[0]
        range_end = r[1]
    if r[1] >= range_start-1:
        if r[0] < range_start:
            range_start = r[0]
full_ranges.append([range_start, range_end]) 

for r in full_ranges:
    counter += r[1] - r[0] + 1
print(counter)