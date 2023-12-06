with open("2023\\5.txt") as fl:
    pointers, *lines = fl.read().strip().split("\n\n")
    pointers = list(map(int, pointers.split(":")[1].split()))

    ranges = [
        (pointers[i], pointers[i] + pointers[i + 1]) for i in range(0, len(pointers), 2)
    ]

for line in lines:
    new_pointers = []
    new_ranges = []

    block = [list(map(int, x.split())) for x in line.splitlines()[1:]]

    for point in pointers:
        for destination, source, step in block:
            if point in range(source, source + step):
                new_pointers.append(destination + point - source)
                break
        else:
            new_pointers.append(point)

    while len(ranges) > 0:
        start, end = ranges.pop()
        for destination, source, step in block:
            overlap_start = max(start, source)
            overlap_end = min(end, source + step)
            # Find start and end of overlap between given block and poped pointer range
            # Refer to the youtube line on line 58 as it has better illustration of the working

            if overlap_start < overlap_end:
                new_ranges.append(
                    (
                        destination + overlap_start - source,
                        destination + overlap_end - source,
                    )
                )

                if overlap_start > start:
                    ranges.append((start, overlap_start))
                if overlap_end < end:
                    ranges.append((overlap_end, end))
                # To account for parts of the pointer range that do not completely overlap under current block

                break
        else:
            new_ranges.append((start, end))

    pointers = new_pointers
    ranges = new_ranges

print(f"Lowest location corresponding to initial seed numbers: {min(pointers)}")
print(f"Lowest location corresponding to new seed ranges: {min(ranges)[0]}")


# print(f"Lowest location corresponding to new seed numbers: {min(seed_map2)}")
# I was unable to brute force my way through Part 2 of Day 5, I ended up having to refer to this youtube video
# (https://www.youtube.com/watch?v=NmxHw_bHhGM&t=895s) to gain clarity on how I had to solve this
# and ended up restructuring my entire program.
