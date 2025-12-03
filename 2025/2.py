def count_valid(lines):
    invalid1 = 0
    invalid2 = 0
    
    for start, end in lines:
        for val in range(start, end+1):
            obj = str(val)
            cache = ""

            for i in obj:
                if cache.startswith(i) and cache * (count := round(len(obj)/len(cache))) == obj:

                    if count % 2 == 0 and cache * count == obj:
                        invalid1 += val

                    invalid2 += val
                    break

                else:
                    cache += i
    
    
    return invalid1, invalid2


with open("2025\\2.txt") as fl:
    lines = [[int(j) for j in i.split("-")] for i in fl.read().strip().split(",")]

part1, part2 = count_valid(lines)
print("Part 1:", part1)
print("Part 2:", part2)