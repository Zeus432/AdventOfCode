with open("6.txt") as fl:
    input = list(fl.read().strip())


for i in range(len(input)):
    if len(input[i : i + 4]) == len(set(input[i : i + 4])):
        print(f"First marker (4) after charecter: {i + 4}")
        break

for i in range(len(input)):
    if len(input[i : i + 14]) == len(set(input[i : i + 14])):
        print(f"First marker (14) after charecter: {i + 14}")
        break
