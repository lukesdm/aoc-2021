# Get (most common, least common) at the given position
def mlcommon(lines, pos):
    oneLines = [] # Lines that have 1 at pos
    zeroLines = []
    for line in lines:
        if line[pos] == '1':
            oneLines.append(line)
        else:
            zeroLines.append(line)
    return ("1", oneLines, zeroLines) if len(oneLines) > len(lines) / 2 else ("0", zeroLines, oneLines)

def calc_o2(lines, pos):
    b, mcLines, lcLines = mlcommon(lines, pos)
    filteredLines = mcLines if len(mcLines) != len(lcLines) else (mcLines if b == "1" else lcLines) 
    nextPos = pos + 1
    return filteredLines[0] if len(filteredLines) == 1 else calc_o2(filteredLines, nextPos)

def calc_co2(lines, pos):
    b, mcLines, lcLines = mlcommon(lines, pos)
    filteredLines = lcLines if len(mcLines) != len(lcLines) else (mcLines if b == "0" else lcLines)
    nextPos = pos + 1
    return filteredLines[0] if len(filteredLines) == 1 else calc_co2(filteredLines, nextPos)

input = None
filename = "day3-input.txt" # "day3-sample.txt"
with open(filename) as reader:
    input = reader.readlines()

formatter = lambda item: item.strip()
lines = list(map(formatter, input))

o2 = calc_o2(lines, 0)
co2 = calc_co2(lines, 0)

print(o2, co2)

result = int(o2, 2) * int(co2, 2)

print(result)