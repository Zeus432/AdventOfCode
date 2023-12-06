with open("2023\\5.txt") as fl:
    pointers, *lines = fl.read().strip().split("\n\n")
    pointers = list(map(int, pointers.split(":")[1].split()))

for line in lines:
    new_pointer = []
    block = [list(map(int, x.split())) for x in line.splitlines()[1:]]

    for point in pointers:
        for destination, source, step in block:
            if point in range(source, source + step):
                new_pointer.append(destination + point - source)
                break
        else:
            new_pointer.append(point)

    pointers = new_pointer

# fmt: off
print(f"Lowest location corresponding to initial seed numbers: {min(pointers)}")
# fmt: on
