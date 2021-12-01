from functools import reduce
from itertools import pairwise

input = None
filename = "day1-input.txt" # "day1-sample.txt" 
with open(filename) as reader:
    input = reader.readlines()

formatter = lambda item: int(item.strip())
seq = list(map(formatter, input))

windowSeq = zip(seq, seq[1:], seq[2:])

windowPairs = pairwise(windowSeq)

countIncreases = lambda count, windowPair: count + 1 if sum(windowPair[1]) > sum(windowPair[0]) else count

result = reduce(countIncreases, windowPairs, 0)

print(result)