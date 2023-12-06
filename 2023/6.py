with open("2023\\6.txt") as fl:
    time, distance = fl.read().strip().split("\n")
    time = list(map(int, time.split(":")[1].split()))
    distance = list(map(int, distance.split(":")[1].split()))

    time.append(int("".join(map(str, time))))
    distance.append(int("".join(map(str, distance))))

net = 1
for i in range((length := len(distance))):
    win = 0
    for speed in range((t := time[i])):
        if speed * (t - speed) > distance[i]:
            win += 1

    net *= 1 if win == 0 or i == length - 1 else win

print(f"Product of number of ways to beat record: {net}")
print(f"Number of ways to beat final record: {win}")
