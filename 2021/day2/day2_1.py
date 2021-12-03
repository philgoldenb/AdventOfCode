def position(instructions):
    depth = 0
    horizontal = 0
    for instr in instructions:
        if instr[0] == "forward":
            horizontal += int(instr[1])
        elif instr[0] == "down":
            depth += int(instr[1])
        elif instr[0] == "up":
            depth -= int(instr[1])

    return horizontal * depth

input_file = "/Users/phil/repos/AdventOfCode/2021/day2/input.txt"
with open(input_file,"r") as file:
    instructions = [l.split() for l in file]


print(position(instructions))