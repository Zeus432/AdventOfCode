with open("4.txt") as fl:
    input = [
        [range(eval(x.split("-")[0]), eval(x.split("-")[1]) + 1) for x in f.split(",")]
        for f in fl.read().strip().split("\n")
    ]

total = len(
    [True for a, b in input if all(x in a for x in b) or all(x in b for x in a)]
)

print(f"{total} pairs completely overlap!")

total = len(
    [True for a, b in input if any(x in a for x in b) or any(x in b for x in a)]
)

print(f"{total} pairs overlap!")
