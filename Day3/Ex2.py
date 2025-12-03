with open('input.txt') as file:
    data = file.readlines()

# Simply get the highest value from a string and return it coupled with its index
def get_max_possible(row):
    highest = '0'
    highest_idx = 0
    i = 0
    for figure in row:
        if figure > highest:
            highest = figure
            highest_idx = i
        i += 1
    return highest, highest_idx

counter = 0
for row in data[:]:
    row = row.strip()
    sub_s_len = 11
    substring = ''
    # Calculate where the next figure can be, take the highest figure from that portion and
    # reduce the row excluding everything before the value selected (included)
    while sub_s_len >= 0:
        s_len = len(row)
        possible_loc = s_len - sub_s_len
        max_pos, highest_idx = get_max_possible(row[:possible_loc])
        substring += max_pos
        row = row[highest_idx+1:]
        sub_s_len -= 1
    counter += int(substring)
print(f'Final: {counter}')