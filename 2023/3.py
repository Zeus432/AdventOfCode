with open("2023\\3.txt") as fl:
    lines = fl.read().strip().split("\n")


def check_surroundings(lines: list, line_index: int, start: int, end: int) -> bool:
    surround = []
    current = lines[line_index]

    surround.extend(
        [
            "." if start == 0 else current[start - 1],
            "." if end == len(current) - 1 else current[end + 1],
        ]
    )  # add value before and after value in current line

    surround.append(
        "."
        if line_index == 0
        else lines[line_index - 1][
            (0 if start == 0 else start - 1) : end
            + (1 if end == len(current) - 1 else 2)
        ]
    )  # add previous line surrounding value

    surround.append(
        "."
        if line_index == len(lines) - 1
        else lines[line_index + 1][
            (0 if start == 0 else start - 1) : end
            + (1 if end == len(current) - 1 else 2)
        ]
    )  # add next line surrounding value

    for char in "".join(surround):
        if char.isdigit() is False and char != ".":
            return True
    return False


net = 0

for index, line in enumerate(lines):
    nxt = -999  # idk man i just like this number
    for i, char in enumerate(line):
        if i <= nxt or char.isdigit() is not True:
            continue

        for n in range(1, len(line) - i):
            if line[i + n].isdigit() is not True:
                val = line[i : i + n]
                nxt = i + n
                net += (
                    int(val)
                    if check_surroundings(lines, index, i, i + n - 1) is True
                    else 0
                )
                break

            elif (i + n) == (len(line) - 1):
                val = line[i : len(line)]
                nxt = i + n
                check_surroundings(lines, index, i, i + n)
                net += (
                    int(val)
                    if check_surroundings(lines, index, i, i + n) is True
                    else 0
                )
                break

print(net)
