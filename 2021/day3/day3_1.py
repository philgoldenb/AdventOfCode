from collections import Counter

INPUT_FILE = 'day3/input.txt'

with open(INPUT_FILE, 'r') as file:
    diagnostics = [line.rstrip() for line in file]
columns = zip(*diagnostics)

gamma, epsilon = "", ""
for column in columns:
    counts = Counter(column)
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