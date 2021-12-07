import math

sample = [3,4,3,1,2]
# ages. 8 -> 0 ... 0 -> 8
initial_ages = [5, 4, 5, 7, 6]

def spawned(age):
    return math.trunc((age-2) / 7)

# Doesn't work.
def total(days):
    gens = spawned(days)
    count = 1 + gens
    for gen in range(1,gens + 1):
        count += gen * spawned(days - 9 - (gen - 1) * 7)
    return count


spawned_tests=[
# (age, expected)
    (0, 0),
    (1, 0),
    (2, 0),
    (3, 0),
    (4, 0),
    (5, 0),
    (6, 0),
    (7, 0),
    (8, 0), 
    (9, 1), 
    (10, 1),
    (11, 1),
    (12, 1),
    (13, 1),
    (14, 1), 
    (15, 1), 
    (16, 2),
    (17, 2),
    (18, 2),
    (19, 2),
    (20, 2),
    (21, 2),
    (22, 2),
    (23, 3),
    (24, 3),
    (25, 3), 
]

print("spawned_tests")
for age, expected in spawned_tests:
    actual = spawned(age)
    print(age, expected, actual, expected == actual)


total_tests = [
    # (age, expected)
    (0, 1),
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 1),
    (5, 1),
    (6, 1),
    (7, 1),
    (8, 1),
    (9, 2),
    (10, 2),
    (11, 2),
    (12, 2),
    (13, 2),
    (14, 2),
    (15, 2),
    (16, 3),
    (17, 3),
    (18, 4),
    (19, 4),
    (20, 4),
    (21, 4),
    (22, 4),
    (23, 5),
    (24, 5),
    (25, 7),
    (26, 7),
    (27, 8),
    (28, 8),
    (29, 8),
    (30, 9),
    (31, 9),
    (32, 12),
    (33, 12),
    (34, 15),
    (35, 15),
    (36, 16),
    (37, 17),
    (38, 17),
    (39, 21),
    (40, 21),
    (41, 27),
    (42, 27),
    (43, 31),
    (44, 32),
    (45, 33),
    (46, 38),
    (47, 38),
    (48, 48),
    (49, 48),
    (50, 58),
]

print("Total tests...")

for age, expected in total_tests:
    actual = total(age)
    print(age, expected, actual, expected == actual)

