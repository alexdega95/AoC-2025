import bisect 

with open('input.txt', 'r') as file:
    data = file.readlines()
to_sort = []
for i, row in enumerate(data):
    if row == '\n':
        to_check = [int(value.strip()) for value in data[i+1:]]
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

end_ranges = [x[1] for x in full_ranges]
for n in to_check:
    range_idx = bisect.bisect_left(end_ranges, n)
    if range_idx < len(full_ranges) and n >= full_ranges[range_idx][0]:
        counter += 1
print(counter)