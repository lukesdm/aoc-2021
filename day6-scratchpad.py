import math

def spawnedByDay(start, day):
    return math.trunc((day - (1 + start - 7))/7)

spawnedByday_tests=[
# (start, day, expected)
    (8, 0, 0),
    (8, 1, 0),
    (8, 2, 0),
    (8, 3, 0),
    (8, 4, 0),
    (8, 5, 0),
    (8, 6, 0),
    (8, 7, 0),
    (8, 8, 0), 
    (8, 9, 1), 
    (8, 10, 1),
    (8, 11, 1),
    (8, 12, 1),
    (8, 13, 1),
    (8, 14, 1), 
    (8, 15, 1), 
    (8, 16, 2),
    (8, 17, 2),
    (8, 18, 2),
    (8, 19, 2),
    (8, 20, 2),
    (8, 21, 2),
    (8, 22, 2),
    (8, 23, 3),
    (8, 24, 3),
    (8, 25, 3), 
    
    (7, 7, 0),
    (7, 8, 1),
    (7, 9, 1),

    (6, 6, 0),
    (6, 7, 1),
    (6, 8, 1),

    (5, 5, 0),
    (5, 6, 1),
    (5, 7, 1),

    (0, 0, 0),
    (0, 1, 1),
    (0, 2, 1),
]

for start, day, expected in spawnedByday_tests:
    actual = spawnedByDay(start, day)
    print(start, day, expected, actual, expected == actual)

# THIS IS WRONG
def total(start, day):
    total = 0
    for generation in range(0, day // 7):
        total += spawnedByDay(start, day - (7 * generation))
    return total

total_tests = [
    # (start, day, expected)
    (8, 0, 1), # remember to count the individual + their spawn
    (8, 1, 1),
    (8, 8, 1), 
    (8, 9, 2), 
    (8, 14, 2),
    (8, 15, 2),
    (8, 16, 3),
    (8, 17, 3), 
    (8, 18, 4), 
    (8, 22, 4),
    (8, 23, 5),
    (8, 24, 5),
    (8, 41, 27)
]

print("Total tests...")