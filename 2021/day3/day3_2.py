from collections import Counter

INPUT_FILE = 'day3/input.txt'

with open(INPUT_FILE,'r') as file:
    contents = file.readlines()

row_len = len(contents[0])

oxy_contents = contents
for col in range(row_len):
    counts = Counter(line[col] for line in oxy_contents)
    most_common_val = "1" if counts["1"] >= counts["0"] else "0"
    oxy_contents = [row for row in oxy_contents if row[col] == most_common_val]
    if len(oxy_contents) == 1:
        break


co2_contents = contents
for col in range(row_len):
    counts = Counter(line[col] for line in co2_contents)
    least_common_val = "1" if counts["1"] < counts["0"] else "0"
    co2_contents = [row for row in co2_contents if row[col] == least_common_val]
    if len(co2_contents) == 1:
        break


oxy_gen = oxy_contents[0]
co2_gen = co2_contents[0]

print(f"oxy_gen is {oxy_gen}")
print(f"co2_gen is {co2_gen}")

print(f"Life Support Rating = {int(oxy_gen, 2) * int(co2_gen, 2)}")