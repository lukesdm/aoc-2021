# Example input:
# up 3
# down 5
# forward 8 
# ...

from functools import reduce

def parse(line):
    tokens = line.strip().split(" ")
    return tokens[0], int(tokens[1])

def move(curr_pos, instruction):
    x, depth, aim = curr_pos
    direction, amt = instruction
    if direction == "forward":
        x = x + amt
        depth = depth + (aim * amt)
    elif direction == "up":
        aim = aim - amt
    elif direction == "down":
        aim = aim + amt
     
    return x, depth, aim

input = None
filename = "day2-input.txt" # "day2-sample.txt"
with open(filename) as reader:
    input = reader.readlines()

seq = map(parse, input)
x, depth, aim = reduce(move, seq, (0,0,0))

print(x, depth, aim)

result = x * depth
print(result)