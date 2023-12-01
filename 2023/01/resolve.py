# -*- coding: utf-8 -*-
DATA_FILE_1 = 'data.in'
DATA_FILE_2 = 'data_2.in'

# this save the case eightwo -> 82
LETTER_2_NUMBER = {"one": "o1e", 
                   "two": "t2o", 
                   "three": "t3e", 
                   "four": "f4r", 
                   "five": "f5e", 
                   "six": "s6x", 
                   "seven": "s7n", 
                   "eight": "e8t", 
                   "nine": "n9e"}

def read_file(filename):
    f = open(filename, "r")
    return f.readlines()

def get_individual_calibration_value(line):
    digits = ""
    for l in line:
        if (l.isdigit()):
            digits += l
    if (len(digits)==1):
        return int(digits + digits)
    else:
        return int(digits[0] + digits[len(digits)-1])

def convert_letters_to_numbers(line):
    for key in LETTER_2_NUMBER.keys():
        line = line.replace(key, LETTER_2_NUMBER[key])
    return line

def part_one():
    lines = read_file(DATA_FILE_1)
    calibration_value = 0
    for line in lines:
        calibration_value += get_individual_calibration_value(line)
    print("PART ONE calibration value: ", calibration_value)


def part_two():
    lines = read_file(DATA_FILE_2)
    calibration_value = 0
    for line in lines:
        final_line = convert_letters_to_numbers(line)
        calibration_value += get_individual_calibration_value(final_line)
    print("PART TWO calibration value: ", calibration_value)


if __name__ == "__main__":
    part_one()
    part_two()