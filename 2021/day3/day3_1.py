INPUT_FILE = 'day3/input.txt'

with open(INPUT_FILE, 'r') as file:
    diagnostics = [line.rstrip() for line in file]

gamma, epsilon = "", ""
for i in range(len(diagnostics[0])):

    counts = {"0": 0, "1": 0}
    for reading in diagnostics:
        counts[reading[i]] += 1

    if counts["0"] > counts["1"]:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

gamma_dec = int(gamma, 2)
epsilon_dec = int(epsilon, 2)

print(gamma_dec * epsilon_dec)