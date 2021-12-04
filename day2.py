# get input
commands = []
with open("day2_input.txt") as f:
    for line in f:
        line = line.split(" ")
        commands.append([line[0], int(line[1])])


def part_1():
    horizontal = 0
    depth = 0
    for line in commands:
        [command, value] = line
        if(command == 'forward'):
            horizontal += value
        elif(command == 'down'):
            depth += value
        elif(command == 'up'):
            depth -= value
            
    return horizontal * depth


def part_2():
    horizontal = 0
    depth = 0
    aim = 0

    for line in commands:
        [command, value] = line
        if(command == 'forward'):
            horizontal += value
            depth += (aim * value) 
        elif(command == 'down'):
            aim += value
        elif(command == 'up'):
            aim -= value
            
    return horizontal * depth


print("Solution Part 1: ", part_1()) # 2147104
print("Solution Part 2: ", part_2()) # 2044620088
