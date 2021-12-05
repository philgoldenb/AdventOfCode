from collections import Counter

INPUT_FILE = 'day3/input.txt'

counters = []
with open(INPUT_FILE, 'r') as file:
    for line in file:
        line = line.rstrip() 
        if not counters:
            counters = [Counter() for _ in range(len(line))]
        for counter, bit in zip(counters, line):
            counter[bit] += 1

gamma, epsilon = "", ""
for counts in counters:
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