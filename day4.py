import numpy as np

# First line of picks, then grids (5x5) separated by blank line.
def parse(lines):
    picks = map(int, lines[0].split(","))
    grids = []
    # 1 grid every 6 lines starting at lines[2]
    parseGrid = lambda l: list(map(int, l.strip().split()))
    end = len(lines) - 4
    for s in range(2, end, 6):
        grid = list(map(parseGrid, lines[s:s+5]))
        npGrid = np.array(grid)
        grids.append(npGrid)
    return picks, grids
    
input = None
filename = "day4-sample.txt" # "day4-input.txt" 
with open(filename) as reader:
    input = reader.readlines()

# formatter = lambda item: int(item.strip())
# seq = map(formatter, input)
picks, grids = parse(input)

print(grids[0][:,0])