with open("2023\\3.txt") as fl:
    lines = fl.read().strip().split("\n")


def check_surroundings(
    lines: list, line_index: int, start: int, end: int
) -> list[str, list[int, int]] | bool:
    surround = []
    current = lines[line_index]

    if start != 0:  # add values on current line before current value
        surround.append([current[start - 1], [line_index, start - 1]])

    if end != len(current) - 1:  # add values on current line after current value
        surround.append([current[end + 1], [line_index, end + 1]])

    if line_index != 0:  # add surrounding values on previous line to current value
        for i in range(
            0 if start == 0 else start - 1, end + (1 if end == len(current) - 1 else 2)
        ):
            surround.append([lines[line_index - 1][i], [line_index - 1, i]])

    # fmt: off
    if line_index != len(lines) - 1:  # add surrounding values on next line to current value # fmt: on
        for i in range(
            0 if start == 0 else start - 1, end + (1 if end == len(current) - 1 else 2)
        ):
            surround.append([lines[line_index + 1][i], [line_index + 1, i]])

    for valset in surround:
        char = valset[0]
        index = valset[1]

        if char.isdigit() is False and char != ".":
            return [char, index]
    return False


def search_gears(
    gear: list, value: str, match: str, x: int, y: int, val: int = 0
) -> int:
    for valset in gear:
        if valset[1:4] == [match, x, y]:
            val = int(valset[0]) * int(value)
    gear.append([value, match, x, y])
    return val


part = 0
gear = []
gear_ratio = 0

for index, line in enumerate(lines):
    nxt = -999  # idk man i just like this number
    for i, char in enumerate(line):
        if i <= nxt or char.isdigit() is not True:
            continue

        for n in range(1, len(line) - i):
            if line[i + n].isdigit() is not True:
                val = line[i : i + n]
                nxt = i + n
                if (
                    valset := check_surroundings(lines, index, i, i + n - 1)
                ) is not False:
                    part += int(val)
                    gear_ratio += search_gears(
                        gear, val, valset[0], valset[1][0], valset[1][1]
                    )
                break

            elif (i + n) == (len(line) - 1):
                val = line[i : len(line)]
                nxt = i + n
                if (valset := check_surroundings(lines, index, i, i + n)) is not False:
                    part += int(val)
                    gear_ratio += search_gears(
                        gear, val, valset[0], valset[1][0], valset[1][1]
                    )
                break

print(f"Sum of all part numbers: {part}")
print(f"Sum of all gear ratios: {gear_ratio}")
