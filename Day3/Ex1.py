with open('input.txt') as file:
    data = file.readlines()

def get_highest(row):
    highest = '0'
    highest_idx = 0
    rown = 0
    for figure in row:
        if figure > highest:
            highest = figure
            highest_idx = rown
        rown += 1
    return highest, highest_idx
counter = 0

for row in data[:]:
    row = row.strip()
    highest, highest_idx = get_highest(row)
    most_valuable = None
    least_valuable = None
    # if the highest number index is in the last position, that figure have to be considered as the least valuable figure
    # in this case, the most valuable figure is the largest figure before the last one
    if highest_idx == len(row) - 1:
       least_valuable = highest
       most_valuable, most_valuable_idx = get_highest(row[:-1])
    # If the highest number index is everywhere but in the last position, it's considered the most valuable figure
    # the other one is the largest that follows 
    else: 
        most_valuable = highest
        least_valuable, least_valuable_idx = get_highest(row[highest_idx+1:]) 
    composed = most_valuable + least_valuable
    counter += int(composed)

print(f'Final: {counter}')