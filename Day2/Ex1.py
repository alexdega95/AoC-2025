with open('input.txt') as file:
    data = file.readline()
data = data.split(',')

# This function avoids to check for invalid IDs where it's impossible to have them (number with odd number of figures)
def check_range(low, high):
    if low == high:
        return [low // 2] 
    return [x // 2 for x in range(low, high + 1) if x % 2 == 0]

counter = 0

for id_range in data:
    low = id_range.split('-')[0]
    high = id_range.split('-')[1]
    len_low = len(low)
    len_high = len(high)


    for l in check_range(len_low, len_high):
        a = 10 ** (l - 1)   
        b = 10 ** l 

        # double the figures of each candidate and check if the resulting number is in range     
        for i in range(a, b):
            candidate = int(str(i) + str(i))
            if candidate >= int(low) and candidate <= int(high):
                counter += candidate

print(f"Invalid IDs sum: {counter}")