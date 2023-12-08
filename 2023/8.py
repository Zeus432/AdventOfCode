from math import lcm

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
        if current_node == "ZZZ":
            break


steps_list = []
for current_node in nodes.keys():
    if current_node.endswith("A"):
        step2 = 0
        while current_node.endswith("Z") is not True:
            for direc in directions:
                current_node = nodes[current_node][0 if direc == "L" else 1]
                step2 += 1
                if current_node.endswith("Z") is True:
                    break
        if step2 != 0:
            steps_list.append(step2)


print(f"Number of steps taken: {steps}")
print(f"Number of steps taken for all nodes: {lcm(*steps_list)}")
