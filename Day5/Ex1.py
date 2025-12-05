with open('input.txt', 'r') as file:
    data = file.readlines()
to_sort = []
for i, row in enumerate(data):
    if row == '\n':
        to_check = [int(value.strip()) for value in data[i+1:]]
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

for n in to_check:
    for r in full_ranges:
        if r[0] <= n <= r[1]:
            counter += 1

print(counter)