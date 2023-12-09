with open("2023\\9.txt") as fl:
    lines = [list(map(int, line.split())) for line in fl.read().strip().split("\n")]

forwards = 0
backwards = 0
for line in lines:
    history = []
    history.append(line)
    while history[-1].count(0) != len(history[-1]):
        history.append(
            [(history[-1][i + 1] - history[-1][i]) for i in range(len(history[-1]) - 1)]
        )

    forwards += sum([sequence[-1] for sequence in history])
    backwards += sum(
        [
            (-1 if index % 2 != 0 else 1) * sequence[0]
            for index, sequence in enumerate(history)
        ]
    )

print(f"Sum of extrapolating forwards: {forwards}")
print(f"Sum of extrapolating backwards: {backwards}")
