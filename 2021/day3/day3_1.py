from collections import Counter, defaultdict

INPUT_FILE = 'day3/input.txt'

counters = defaultdict(Counter)
with open(INPUT_FILE, 'r') as file:
    for line in file:
        line = line.rstrip() 
        for col, bit in enumerate(line):
            counters[col][bit] += 1

gamma, epsilon = "", ""
for col in range(len(line)):
    bit, _ = counters[col].most_common(1)[0]
    if bit == "0":
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

gamma_dec = int(gamma, 2)
epsilon_dec = int(epsilon, 2)

print(gamma_dec * epsilon_dec)