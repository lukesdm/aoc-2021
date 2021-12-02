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
    x, depth = curr_pos
    direction, amt = instruction
    if direction == "forward":
        x = x + amt
    elif direction == "up":
        depth = depth - amt
    elif direction == "down":
        depth = depth + amt
     
    return x, depth

input = None
filename = "day2-input.txt" # "day2-sample.txt" 
with open(filename) as reader:
    input = reader.readlines()

seq = map(parse, input)
x, depth = reduce(move, seq, (0,0))

print(x, depth)

result = x * depth
print(result)