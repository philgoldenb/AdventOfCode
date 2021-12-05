
INPUT_FILE = 'day3/input.txt'

with open(INPUT_FILE, 'r') as file:
    #contents = file.readlines()
    diagnostics = [line.rstrip() for line in file]

gamma, epsilon = "", ""
for i in range(len(diagnostics[0])):
    count_0s, count_1s = 0, 0

    for reading in diagnostics:
        if reading[i] == "0":
            count_0s += 1
        elif reading[i] == "1":
            count_1s += 1
    
    most_common_bit = "1" if count_1s >= count_0s else "0"
    least_common_bit = "0" if count_1s >= count_0s else "1"

    gamma += most_common_bit
    epsilon += least_common_bit

gamma_dec = int(gamma, 2)
epsilon_dec = int(epsilon, 2)

print(gamma_dec * epsilon_dec)