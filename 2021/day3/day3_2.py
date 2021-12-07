from collections import Counter
import operator

INPUT_FILE = 'day3/input.txt'

with open(INPUT_FILE,'r') as file:
    contents = file.readlines()

def compute_rating(contents, filter_criteria):
    row_len = len(contents[0])

    for col in range(row_len):
        counts = Counter(line[col] for line in contents)
        filter_val = "1" if filter_criteria(counts["1"], counts["0"]) else "0"
        contents = [row for row in contents if row[col] == filter_val]

        if len(contents) == 1:
            break
    
    return contents[0]

oxy_gen = compute_rating(contents, operator.ge)
co2_gen = compute_rating(contents, operator.lt)

print(f"oxy_gen is {oxy_gen}")
print(f"co2_gen is {co2_gen}")

print(f"Life Support Rating = {int(oxy_gen, 2) * int(co2_gen, 2)}")