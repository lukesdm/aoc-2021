import re

def parse(txt):
    matches = re.search(r"(\d+),(\d+) -> (\d+),(\d+)", txt)
    x1 = int(matches.group(1))
    y1 = int(matches.group(2))
    x2 = int(matches.group(3))
    y2 = int(matches.group(4))
    return x1, y1, x2, y2

def cells(xMax, yMax):
    for y in range(0, yMax+1):
        for x in range(0,xMax+1):
            yield (x, y)

def is_v_line(line):
    x1, _, x2, _ = line
    return x1 == x2

def is_h_line(line):
    _, y1, _, y2 = line
    return y1 == y2

def intersect(line, cell):
    x1, y1, x2, y2 = line
    px, py = cell
    if is_v_line(line):
        return px == x1 and ((y1 <= py <= y2) or (y2 <= py <= y1))
    elif is_h_line(line):
        return py == y1 and ((x1 <= px <= x2) or (x2 <= px <= x1))
    else:
        return False
    
input = None
filename = "day5-input.txt" # "day5-sample.txt" 
with open(filename) as reader:
    input = reader.readlines()

xMax = 0
yMax = 0
lines = []
for txt in input:
    line = parse(txt)
    lines.append(line)
    
    if line[0] > xMax:
        xMax = line[0]
    if line[2] > xMax:
        xMax = line[2]
    if line[1] > yMax:
        yMax = line[1]
    if line[3] > yMax:
        yMax = line[3]

totalOverlaps = 0
for cell in cells(xMax, yMax):
    cellOverlaps = 0
    for line in lines:
        if intersect(line, cell):
            cellOverlaps += 1
            # print(cell, line, cellOverlaps, totalOverlaps)
    if cellOverlaps >= 2:
        totalOverlaps += 1
        
print(totalOverlaps)