report = open("day3_input.txt").read().splitlines()

# power consumption = gamma rate * epsilon rate

def part_1():
    gamma_rate = '0b'
    epsilon_rate = '0b'
    for i in range(0, len(report[0])):
        zero = 0
        one = 0
        for line in report:
            if(line[i] == '0'):
                zero += 1
            elif(line[i] == '1'):
                one += 1
        if(zero > one):
            gamma_rate += '0'
            epsilon_rate += '1'
        elif(zero < one):
            gamma_rate += '1'
            epsilon_rate += '0'
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


# life support rating = oxygen generator rating * CO2 scrubber rating

def part_2():

    def get_numbers_with_bit(arr, i,  bit):
        new_arr = []
        for line in arr:
            if(line[i] == bit):
                new_arr.append(line)
        return new_arr

    def find_rating(arr, type, i=0):
        if(len(arr) == 1):
            return arr[0]

        zero = 0
        one = 0
        for line in arr:
            if(line[i] == '0'):
                zero += 1
            else: 
                one += 1
        if(zero > one):
            if(type == 'oxygen_generator'):
                new_arr = get_numbers_with_bit(arr, i, '0')
            else:
                new_arr = get_numbers_with_bit(arr, i, '1')
        else:
            if(type == 'oxygen_generator'):
                new_arr = get_numbers_with_bit(arr, i, '1')
            else:
                new_arr = get_numbers_with_bit(arr, i, '0')
                
        
        return find_rating(new_arr, type, i + 1)


    oxygen_generator_rating = find_rating(report, 'oxygen_generator')
    co2_scrubber_rating = find_rating(report, 'co2_scrubber')

    oxygen_generator_rating = '0b' + oxygen_generator_rating
    co2_scrubber_rating = '0b' + co2_scrubber_rating


    return int(oxygen_generator_rating, 2) * int(co2_scrubber_rating,2)

print("Solution Part 1: ", part_1()) # 3958484
print("Solution Part 2: ", part_2()) # 1613181
