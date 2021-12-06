from collections import Counter, defaultdict

INPUT_FILE = 'day3/input.txt'

counts = Counter()
with open(INPUT_FILE, 'r') as file:
    for line in file:
        counts += Counter(enumerate(line.rstrip()))
print(counts)

gamma, epsilon = "", ""
for col in range(len(counts) // 2):
    count_0s, count_1s = counts[(col, "0")], counts[col,"1"]
    if count_0s > count_1s:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

gamma_dec = int(gamma, 2)
epsilon_dec = int(epsilon, 2)

print(gamma_dec * epsilon_dec)