with open('input.txt/mnt/Storage/Uni/Progettini/adventOfCode25/Day5/input.txt', 'r') as file:
    data = file.readlines()
to_sort = []
for row in data:
    if row == '\n':
        break
    vals = row.strip().split('-')
    to_sort.append([int(vals[0]), int(vals[1])])
sorted_ranges = sorted(to_sort, key= lambda x: x[0])

counter = 0
full_ranges = []

start, end = sorted_ranges[0]
for r in sorted_ranges[1:]:
    if r[0] <= end + 1:
        end = max(r[1], end)
        continue
    full_ranges.append([start, end])
    start, end = r
full_ranges.append([start, end])


for r in full_ranges:
    counter += r[1] - r[0] + 1
print(counter)