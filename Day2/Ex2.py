with open('input.txt') as file:
    data = file.readline()
data = data.split(',')

counter = 0

for id_range in data:
    low = int(id_range.split('-')[0])
    high = int(id_range.split('-')[1])
    # avoid double counting
    valid_numbers_in_range = set()
    q = len(str(high)) // 2

    # the idea is similar to the one used in exercise 1 but candidates with length less than half the size of the number have to be checked    
    for i in range(1, q + 1):
        start = 10 ** (i - 1)
        end = 10 ** i
        for candidate in range(start, end):
            candidate = str(candidate)
            current = candidate * 2
            while True:
                current_i = int(current)
                if current_i > high:
                    break
                if current_i >= low:
                    # Add to set instead of counting directly to avoid double counting
                    valid_numbers_in_range.add(current_i)
                current += candidate
    counter += sum(valid_numbers_in_range) 
print(counter)