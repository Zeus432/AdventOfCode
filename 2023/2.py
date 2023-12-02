with open("2023\\2.txt") as fl:
    lines = [
        {
            int(line.split(": ")[0].split(" ")[-1]): [
                game.split(", ") for game in line.split(": ")[1].split("; ")
            ]
        }
        for line in fl.read().strip().split("\n")
    ]  # yea i just like doing shi like this instead


def func(match_id: int, match: list[list[str]]) -> int:
    ballval = {"red": [], "green": [], "blue": []}

    for game in match:
        for ball in game:
            ballval[ball.split(" ")[1]].append(int(ball.split(" ")[0]))

    val1 = (
        match_id
        if max(ballval["red"]) <= 12
        and max(ballval["green"]) <= 13
        and max(ballval["blue"]) <= 14
        else 0
    )
    val2 = max(ballval["red"]) * max(ballval["green"]) * max(ballval["blue"])

    return [val1, val2]


result = [func(list(line.keys())[0], line[list(line.keys())[0]]) for line in lines]
net1 = sum(i[0] for i in result)
net2 = sum(i[1] for i in result)


print(f"Sum of IDs of eligible games: {net1}")
print(f"Sum of the power of the sets: {net2}")
