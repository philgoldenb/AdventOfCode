from collections import Counter

INPUT_FILE = 'day3/input.txt'

with open(INPUT_FILE, 'r') as file:
    diagnostics = [line.rstrip() for line in file]

gamma, epsilon = "", ""
for i in range(len(diagnostics[0])):

    counts = Counter()
    for reading in diagnostics:
        counts[reading[i]] += 1

    bit, _ = counts.most_common(1)[0]
    if bit == "0":
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

gamma_dec = int(gamma, 2)
epsilon_dec = int(epsilon, 2)

print(gamma_dec * epsilon_dec)