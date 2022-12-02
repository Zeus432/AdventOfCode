with open("input.in") as fl:
    input = [f.split(" ") for f in fl.read().strip().split("\n")]

points = sum([{"A": {"X": 4, "Y": 8, "Z": 3}, "B": {"X": 1, "Y": 5, "Z": 9}, "C": {"X": 7, "Y": 2, "Z": 6}}[round[0]][round[1]] for round in input])
print(f"According to assumed strategy your points will be: {points}")

print("-"*55)

points = sum([{"A": {"X": 3, "Y": 4, "Z": 8}, "B": {"X": 1, "Y": 5, "Z": 9}, "C": {"X": 2, "Y": 6, "Z": 7}}[round[0]][round[1]] for round in input])
print(f"According to actual strategy your points will be: {points}")