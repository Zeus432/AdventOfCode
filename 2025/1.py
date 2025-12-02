with open("2025\\1.txt") as fl:
    lines = [[i[0], int(i[1:])] for i in fl.read().strip().split("\n")]

num = 50
counter = 0
counter2 = 0

def count_zeros(lines, start=50):
    num = start
    count1 = 0
    count2 = 0
    
    for direction, val in lines:

        if direction == "L":
            limit = num if num != 0 else 100
        
        elif direction == "R":
            limit = 100 - num
        
        if val >= limit:
            count2 += 1 + (val - limit) // 100
        
        num = (num + val) if direction == "R" else (num - val)
        num %= 100

        if num == 0:
            count1 += 1
    
    return count1, count2

part1, part2 = count_zeros(lines, 50)
print("Part 1:", part1)
print("Part 2:", part2)