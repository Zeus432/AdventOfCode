with open("2023\\1.txt") as fl:
    lines = fl.read().strip().split("\n")

DIGITS = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

net1 = 0
net2 = 0


for line in lines:
    num1 = []
    num2 = []

    for index, char in enumerate(line):
        if char.isdigit() is True:
            num1.append(int(char))
            num2.append(int(char))

        for i, num in enumerate(DIGITS):
            if line[index:].startswith(num):
                num2.append(i + 1)

    net1 += num1[0] * 10 + num1[-1]
    net2 += num2[0] * 10 + num2[-1]


print(f"Sum of calibration values: {net1}")
print(f"Sum of real calibration values: {net2}")
