with open("1.txt") as fl:
    calories = {
        i + 1: sum([int(f) for f in x.split("\n")])
        for i, x in enumerate(fl.read().strip().split("\n\n"))
    }


max_vals = sorted(calories, key=calories.get, reverse=True)[:3]

print(f"Fairy {max_vals[0]} is carrying the most calories - {calories[max_vals[0]]}")

sum = 0
print("\nTop 3 Fairies:")
for i in max_vals:
    print(f"Fairy {i} - {calories[i]}")
    sum += calories[i]

print(f"Total {sum} calories")
