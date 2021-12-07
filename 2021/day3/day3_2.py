from collections import Counter

INPUT_FILE = 'day3/input.txt'

with open(INPUT_FILE,'r') as file:
    oxy_contents = [line.strip() for line in file]
co2_contents = [line for line in oxy_contents]

row_len = len(oxy_contents[0])

for col in range(row_len):
    oxy_counts = Counter()

    for line in oxy_contents:
        oxy_counts[line[col]] += 1

    zeros, ones = oxy_counts["0"], oxy_counts["1"]

    if ones >= zeros:
        oxy_contents = [row for row in oxy_contents if row[col] == "1"]
    else:
        oxy_contents = [row for row in oxy_contents if row[col] == "0"]

    if len(oxy_contents) == 1:
        break


for col in range(row_len):
    
    co2_counts = Counter()
    for line in co2_contents:
        co2_counts[line[col]] += 1
    
    zeros, ones = co2_counts["0"], co2_counts["1"]

    if zeros <= ones:
        co2_contents = [row for row in co2_contents if row[col] == "0"]
    else:
        co2_contents = [row for row in co2_contents if row[col] == "1"]
    
    if len(co2_contents) == 1:
        break


oxy_gen = oxy_contents[0]
co2_gen = co2_contents[0]

print(f"oxy_gen is {oxy_gen}")
print(f"co2_gen is {co2_gen}")

print(f"Life Support Rating = {int(oxy_gen, 2) * int(co2_gen, 2)}")