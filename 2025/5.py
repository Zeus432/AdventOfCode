def fresh(lines):
    freshid = 0
    freshtotal = 0
    ranges = []

    for item in lines[1]:
        for start, end in [[int(k) for k in j.split("-")] for j in lines[0]]:
            if int(item) >= start and int(item) <= end:
                freshid += 1
                break

    for start, end in [[int(k) for k in j.split("-")] for j in lines[0]]:
        contained = 0

        for x, y in ranges.copy():
            if start >= x and end <= y:
                contained = 1
                break

            elif start >= x and start <= y and end > y:
                start = y + 1

            elif start < x and end >= x and end <= y:
                end = x - 1

            elif (start > y and end > y) or (start < x and end < y):
                pass

        if contained != 1:
            ranges.append([start, end])

        if len(ranges) == 0:
            ranges.append([start, end])

    for start, end in ranges:
        freshtotal += end + 1 - start

    return freshid, freshtotal


with open("2025\\5.txt") as fl:
    lines = [i.split("\n") for i in fl.read().strip().split("\n\n")]

part1, part2 = fresh(lines)
print("Part 1:", part1)
print("Part 2:", part2)
