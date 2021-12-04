def position(instructions):

    horizontal, depth = 0, 0
    for instruction in instructions:
        direction, value = instruction.split() 
        value = int(value)

        if direction == "forward":
            horizontal += value
        elif direction == "down":
            depth += value
        elif direction == "up":
            depth -= value
        else:
            raise ValueError("Invalid Direction")

    return horizontal * depth

input_file = "/Users/phil/repos/AdventOfCode/2021/day2/input.txt"
with open(input_file,"r") as file:
    instructions = file.readlines()


print(position(instructions))