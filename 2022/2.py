with open("2.txt") as fl:
    input = fl.read().strip().split("\n")

points = sum(
    [
        {
            "A X": 4,
            "A Y": 8,
            "A Z": 3,
            "B X": 1,
            "B Y": 5,
            "B Z": 9,
            "C X": 7,
            "C Y": 2,
            "C Z": 6,
        }[round]
        for round in input
    ]
)
print(f"According to assumed strategy your points will be: {points}")

points = sum(
    [
        {
            "A X": 3,
            "A Y": 4,
            "A Z": 8,
            "B X": 1,
            "B Y": 5,
            "B Z": 9,
            "C X": 2,
            "C Y": 6,
            "C Z": 7,
        }[round]
        for round in input
    ]
)
print(f"According to actual strategy your points will be: {points}")
