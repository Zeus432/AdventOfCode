from collections import defaultdict


with open("test.txt") as fl:
    inp = fl.read().strip().split("\n")

print(inp)

directory = defaultdict(int)
route = []

for command in inp:
    cmd = command.split(" ")
    if command.startswith("$ ls") or command.startswith("dir"):
        continue
    if command.startswith("$ cd"):
        if cmd[2] == "/":
            route = []
        elif cmd[2] == "..":
            route.pop()

        else:
            route.append(cmd[2])
    else:
        print(5)
        print(cmd)
        for i in range(len(route)):
            directory["/" + "/".join(route[:i+1])] += int(cmd[0])

print(sum([dir for dir in directory.values() if dir < 100000]))
