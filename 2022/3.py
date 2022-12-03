def common(a: str, b: str, c: str = "") -> str:
    for char in a:
        if char in b and char in (c or b):
            return v - 96 if (v := ord(char)) >= 97 else v - 38


def split(a: list):
    return sum(
        [common(a[n * 3], a[n * 3 + 1], a[n * 3 + 2]) for n in range(len(a) // 3)]
    )


with open("3.txt") as fl:
    input = fl.read().strip().split("\n")
    m = sum([common(s[: len(s) // 2], s[len(s) // 2 :]) for s in input])
    s = split(input)

print(f"Sum of the priorities: {m}")
print(f"Sum of the group priorities: {s}")
