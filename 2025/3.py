def max_joltage(lines):
    jolt1 = 0
    jolt2 = 0

    for line in lines:
        max1 = 0
        max2 = ""
        start = 0

        for index, a in enumerate(line):
            for b in line[index + 1 :]:
                if (c := int(a + b)) > max1:
                    max1 = c

        for gap in range(12, 0, -1):
            work = line[start : (-gap) + 1] if (-gap) + 1 < 0 else line[start:]

            cache = -1

            for index, x in enumerate(work):
                if int(x) > cache:
                    cache = int(x)
                    temp = index + 1

            start += temp
            max2 += str(cache)

        jolt1 += max1
        jolt2 += int(max2)

    return jolt1, jolt2


with open("2025\\3.txt") as fl:
    lines = fl.read().strip().split("\n")

part1, part2 = max_joltage(lines)
print("Part 1:", part1)
print("Part 2:", part2)
