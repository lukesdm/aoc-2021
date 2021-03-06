import re

def parse(txt):
    matches = re.search(r"(\d+),(\d+) -> (\d+),(\d+)", txt)
    x1 = int(matches.group(1))
    y1 = int(matches.group(2))
    x2 = int(matches.group(3))
    y2 = int(matches.group(4))
    return x1, y1, x2, y2

def is_v_line(line):
    x1, _, x2, _ = line
    return x1 == x2

def is_h_line(line):
    _, y1, _, y2 = line
    return y1 == y2
    
input = None
filename = "day5-input.txt" # "day5-sample.txt"
with open(filename) as reader:
    input = reader.readlines()

lines = []
for txt in input:
    line = parse(txt)
    lines.append(line)

def points(line):
    x1, y1, x2, y2 = line

    if is_h_line(line):
        xs = x1 if x1 <= x2 else x2
        xe = x2 if x1 <= x2 else x1
        for x in range(xs, xe + 1): 
            yield x, y1
    elif is_v_line(line):
        ys = y1 if y1 <= y2 else y2
        ye = y2 if y1 <= y2 else y1
        for y in range(ys, ye + 1):
            yield x1, y

grid = {}
for line in lines:
    for point in points(line):
        grid.setdefault(point, 0)
        grid[point] += 1

totalOverlaps = 0
for v in grid.values():
    if v >= 2:
        totalOverlaps += 1
     
print(totalOverlaps)