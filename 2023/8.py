with open("2023\\8.txt") as fl:
    directions, sp, *nodes = fl.read().strip().split("\n")

directions = list(directions)
nodes = [node.split(" = ") for node in nodes]


nodes = {start: end[1:-1].split(", ") for start, end in nodes}


current_node = "AAA"
steps = 0
while current_node != "ZZZ":
    for direc in directions:
        current_node = nodes[current_node][0 if direc == "L" else 1]
        steps += 1

print(f"Number of steps taken: {steps}")
