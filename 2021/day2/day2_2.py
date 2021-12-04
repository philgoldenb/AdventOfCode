from enum import Enum

INPUT_FILE = "/Users/phil/repos/AdventOfCode/2021/day2/input.txt"

class Direction(Enum):
    FORWARD = 'forward'
    DOWN = 'down'
    UP = 'up'

def parse_instruction(instruction):
    direction, value = instruction.split()
    direction = Direction(direction)
    return direction, int(value)

horizontal, depth, aim = 0, 0, 0

with open(INPUT_FILE, "r") as file:
    for instruction in file:
        direction, value = parse_instruction(instruction)

        if direction == Direction.FORWARD:
            horizontal += value
            depth += aim * value
        elif direction == Direction.DOWN:
            aim += value
        elif direction == Direction.UP:
            aim -= value
        else:
            raise ValueError("Invalid Direction")

    print (horizontal * depth)