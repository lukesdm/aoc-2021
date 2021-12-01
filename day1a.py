from functools import reduce
from itertools import pairwise

input = None
filename = "day1-input.txt" # "day1-sample.txt" 
with open(filename) as reader:
    input = reader.readlines()

formatter = lambda item: int(item.strip())
seq = map(formatter, input)

pairs = pairwise(seq)

countIncreases = lambda count, pair: count + 1 if pair[1] > pair[0] else count

result = reduce(countIncreases, pairs, 0)

print(result)