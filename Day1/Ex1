# Password is defined as a counter, so we initialize it to 0
password = 0

# This function wraps a number in a positive range specified by wrap_limit
def wrap(n, wrap_limit):
    if (n > wrap_limit) | (n < 0) :
        n %= (wrap_limit + 1)
    return n

# Read input file
with open('input.txt') as file:
    input = file.readlines()

# Set dial to initial position
dial = 50

# Loop over the input, adding the number if the dial moves right 
# or subtracting it if it moves left, wrapping the result if it goes out of bounds
for instruction in input:
    if instruction[0] == 'R':
        dial += int(instruction[1:])
        dial = wrap(dial, 99)
    else: 
        dial -= int(instruction[1:])
        dial = wrap(dial, 99)

    if dial == 0:
        password += 1

print(f'Password: {password}')