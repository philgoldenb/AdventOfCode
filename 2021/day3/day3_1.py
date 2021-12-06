from collections import Counter, defaultdict

INPUT_FILE = 'day3/input.txt'

counts = Counter()
with open(INPUT_FILE, 'r') as file:
    for line in file:
        counts += Counter(enumerate(line.rstrip()))

line_len = len(counts) // 2
gamma = ["0" for _ in range(line_len)]
epsilon = gamma[::]
for col in range(line_len):
    count_0s, count_1s = counts[(col, "0")], counts[col,"1"]
    if count_0s > count_1s:
        epsilon[col] = "1"
    else:
        gamma[col] = "1"

gamma_dec = int("".join(gamma), 2)
epsilon_dec = int("".join(epsilon), 2)

print(gamma_dec * epsilon_dec)