import math

def totalDist(crabs, pos):
    total = 0
    for crab in crabs:
        total += abs(crab - pos)
    return total

input = None
filename = "day7-input.txt" # "day7-sample.txt"
with open(filename) as reader:
    input = reader.read()

crabs = list(map(int, input.strip().split(",")))

cmin, cmax = min(crabs), max(crabs)

fuelMin = math.inf
for pos in range(cmin, cmax + 1):
    fuelMin = min(fuelMin, totalDist(crabs, pos))

print(fuelMin)