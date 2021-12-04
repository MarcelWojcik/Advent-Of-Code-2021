report = list(map(int, open("day1_input.txt")))

def part_1():
    counter = 0
    last = report[0]
    for read in report:
        if(read > last):
            counter += 1
        last = read
    return counter

def part_2():
    counter = 0
    for i in range(0, len(report) - 3):
        if(report[i + 3] > report[i]):
            counter += 1
    return counter

print("Solution Part 1: ", part_1()) # 1233
print("Solution Part 2: ", part_2()) # 1275