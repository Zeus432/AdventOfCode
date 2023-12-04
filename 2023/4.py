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

for line in lines:
    win = 0
    points = 0
    for val in line[0]:
        if val in line[1]:
            win += 1
            points = points * 2 if win != 1 else 1
    net_points += points

print(f"Sum of all points: {net_points}")
