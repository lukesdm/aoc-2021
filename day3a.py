input = None
filename = "day3-input.txt" # "day3-sample.txt" 
with open(filename) as reader:
    input = reader.readlines()

formatter = lambda item: item.strip()
lines = list(map(formatter, input))
lineLen = len(lines[0])

# Get (most common, least common) bit at the given position
def mlcommon(pos):
    oneCount = 0
    for line in lines:
        if line[pos] == '1':
            oneCount = oneCount + 1
    return ("1", "0") if oneCount > len(lines) / 2 else ("0", "1")

gamma_bits = ""
epsilon_bits= ""

for pos in range(0, lineLen):
    mcb, lcb = mlcommon(pos)
    gamma_bits += mcb
    epsilon_bits += lcb

print(gamma_bits, epsilon_bits)

result = int(gamma_bits, 2) * int(epsilon_bits, 2)

print(result)