from collections import Counter

INPUT_FILE = 'day3/input.txt'

counts = Counter()
with open(INPUT_FILE, 'r') as file:
    for line in file:
        counts += Counter(enumerate(line.rstrip()))

gamma, epsilon = 0, 0
total_bits = len(counts) // 2
for col in range(total_bits):
    if counts[(col, "0")] > counts[col, "1"]:
        epsilon |= 1 << (total_bits - col - 1)
    else:
        gamma |= 1 << (total_bits - col - 1)

print(gamma * epsilon)