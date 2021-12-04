INPUT_FILE = "/Users/phil/repos/AdventOfCode/2021/day2/input.txt"

horizontal, depth, aim = 0, 0, 0

with open(INPUT_FILE, "r") as file:
    for instruction in file:
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

    print (horizontal * depth)