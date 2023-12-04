import re

with open("2023\\4.txt") as fl:
    lines = [
        [
            re.findall("[0-9]+", line.split(": ")[1].split(" | ")[0]),
            re.findall("[0-9]+", line.split(": ")[1].split(" | ")[1]),
        ]
        for line in fl.read().strip().split("\n")
    ]

net_points = 0
card_count = [1]

for index, line in enumerate(lines):
    win = 0
    points = 0
    for val in line[0]:
        if val in line[1]:
            win += 1
            points = points * 2 if win != 1 else 1
    net_points += points

    if len(card_count) <= index:
        card_count.append(1)

    for i in range(1, win + 1):
        if len(card_count) > index + i:
            card_count[index + i] += 1 * card_count[index]

        else:
            card_count.append(1 + 1 * card_count[index])


print(f"Sum of all points: {net_points}")
print(f"Total number of scratchboards: {sum(card_count)}")
