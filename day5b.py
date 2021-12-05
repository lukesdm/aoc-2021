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

def direction(line):
    x1, y1, x2, y2 = line
    dx = 0 if x2 == x1 else 1 if x2 > x1 else -1
    dy = 0 if y2 == y1 else 1 if y2 > y1 else -1
    return dx, dy  

def points(line):
    x1, y1, x2, y2 = line
    dx, dy = direction(line)
    xs, xend = (x1, x2) if x1 <= x2 else (x2, x1)
    ys, yend = (y1, y2) if y1 <= y2 else (y2, y1)
    x = x1
    y = y1
    while xs <= x <= xend and ys <= y <= yend:
        yield x, y
        x += dx
        y += dy

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