with open("2023\\5.txt") as fl:
    lines = fl.read().strip().split("\n")

    directory = {}

    for index, line in enumerate(lines):
        if line.startswith("seeds:"):
            directory.update(
                {
                    "seeds": [
                        int(seed) for seed in line.split("seeds: ", 1)[1].split(" ")
                    ]
                }
            )

        elif ":" in line:
            _list = []
            for i in range(1, len(lines)):
                if (
                    index + i < len(lines)
                    and ":" not in (x := lines[index + i])
                    and x != ""
                ):
                    _list.append([int(num) for num in x.split(" ")])
                else:
                    directory.update({line[:-5]: _list})
                    break


def link(directory: dict, source: str, destination: str, value: int) -> int:
    for maps in directory[source + "-to-" + destination]:
        if value in (x := range(maps[1], maps[1] + maps[2])):
            return maps[0] + x.index(value)

    return value


seed_map = []
values = [
    "seed",
    "soil",
    "fertilizer",
    "water",
    "light",
    "temperature",
    "humidity",
    "location",
]


for seed in directory["seeds"]:
    _info = {"seed": seed}
    for x in range(len(values) - 1):
        _info.update(
            {values[x + 1]: link(directory, values[x], values[x + 1], _info[values[x]])}
        )
    seed_map.append(_info)

# fmt: off
print(f"Lowest location corresponding to initial seed numbers: {min([seed['location'] for seed in seed_map])}")
# fmt: on
