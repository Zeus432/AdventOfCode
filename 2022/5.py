import re
import copy

with open("5.txt") as fl:
    input = fl.read().rstrip()

rawstack = input[: input.index("\n\nmove")].split("\n")
instructions = [
    [eval(num) for num in re.findall(r"[0-9]+", f)]
    for f in input[input.index("move") :].split("\n")
]

stacks = {eval(i): [] for i in rawstack[-1].split("  ")}
for val in [i[1::4] for i in rawstack[:-1]]:
    for index, char in enumerate(val):
        if char != " ":
            stacks[index + 1].append(char)

stacks2 = copy.deepcopy(stacks)

for move, old, new in instructions:
    for n in range(move):
        val = stacks[old].pop(0)
        stacks[new].insert(0, val)

        val = stacks2[old].pop(0 + (move - n - 1))
        stacks2[new].insert(0, val)

print(
    "The message to be given for Crane 9000:", "".join([i[0] for i in stacks.values()])
)
print(
    "The message to be given for Crane 9001:", "".join([i[0] for i in stacks2.values()])
)
