# Password is defined as a counter, so we initialize it to 0
password = 0

with open('input.txt') as file:
    data = file.readlines()

# Set initial position at 50
absolute = 50

for instruction in data:
    prev_sector = absolute // 100
    amount = int(instruction[1:])
    start_on_zero = (absolute % 100 == 0)

    # Decrease if the instruction goes left, increase if it goes right
    if instruction[0] == 'L':
        absolute -= amount
        curr_sector = absolute // 100
        # If the amount change triggers sector crossing, it means that we passed from 0
        diff = abs(curr_sector - prev_sector)
        # If we've changed sector but we started from 0, we need to decrease the number of crossings
        if start_on_zero and diff > 0:
            diff -= 1
        # If we don't change sector but land on 0 (arriving from right) we need to increase the number of crossings
        if absolute % 100 == 0:
            diff += 1
    else: 
        absolute += amount
        curr_sector = absolute // 100
        diff = abs(curr_sector - prev_sector)
    
    # increase password using number of times we've hit 0
    password += diff

print(f"Password: {password}")