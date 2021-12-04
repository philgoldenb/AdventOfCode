def position(instructions):

    horizontal, depth, aim = 0, 0, 0
    for instruction in instructions:
        direction, value = instruction.split() 
        value = int(value)

        if direction == "forward":
            horizontal += value
            depth += aim * value
        elif direction == "down":
            aim += value
        elif direction == "up":
            aim -= value
        else:
            raise ValueError("Invalid Direction")

    return horizontal * depth

input_file = "/Users/phil/repos/AdventOfCode/2021/day2/input.txt"
with open(input_file,"r") as file:
    instructions = file.readlines()


print(position(instructions))