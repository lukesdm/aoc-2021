def tick(fishList):
    for i, fish in enumerate(fishList):
        if fish == 0:
            fishList.append(9)
            fishList[i] = 6
        else:
            fishList[i] -= 1

input = None
filename = "day6-sample.txt" # "day6-input.txt" # 
with open(filename) as reader:
    input = reader.read()

# fishList = list(map(int, input.strip().split(",")))
fishList = [8]

print(fishList)

for i in range(0,51):
    print(f"({i}, {len(fishList)}),")
    tick(fishList)

# print(fishList)

result = len(fishList)

print(result)