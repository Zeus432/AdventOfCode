with open("2023\\7.txt") as fl:
    lines = [line.split() for line in fl.read().strip().split("\n")]

card_map = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}


def counter(cards: str):
    count = [list(cards).count(char) for char in cards]
    if max(count) > 3:
        return max(count) + 1
    elif max(count) == 3 and 2 in count:
        return 4
    elif max(count) == 3:
        return 3
    elif count.count(2) == 4:
        return 2
    elif max(count) == 2:
        return 1
    return 0


def replacements(hand):
    if hand == "":
        return [""]

    return [
        x + y
        for x in ("23456789TQKA" if hand[0] == "J" else hand[0])
        for y in replacements(hand[1:])
    ]


def classify(hand):
    return max(map(counter, replacements(hand)))


def preference(cards: str):
    return (counter(cards), [card_map.get(card, card) for card in cards])


lines.sort(key=lambda line: preference(line[0]))

net = 0
for rank, (cards, bid) in enumerate(lines, 1):
    net += rank * int(bid)

print(f"Total winnings: {net}")


def preference(cards: str):
    return (classify(cards), [card_map.get(card, card) for card in cards])


lines.sort(key=lambda line: preference(line[0]))


net = 0
for rank, (cards, bid) in enumerate(lines, 1):
    net += rank * int(bid)

print(f"Total winnings (joker): {net}")


# Figure it out
