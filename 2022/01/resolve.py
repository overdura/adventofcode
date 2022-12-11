# -*- coding: utf-8 -*-
DATA_FILE='data.in'

def read_file():
    f = open(DATA_FILE, "r")
    return f.readlines()

def part_one():
    lines = read_file()

    total_calories = 0
    actual_calories = 0
    for line in lines:
        if line == '\n':
            if (actual_calories > total_calories):
                total_calories = actual_calories
            actual_calories = 0
        else: 
            actual_calories += int(line)

    print("PART ONE total calories: ", str(total_calories))

def part_two():
    lines = read_file()

    total_calories = []
    actual_calories = 0
    for line in lines:
        if line == '\n':
            total_calories.append(actual_calories)
            actual_calories = 0
        else: 
            actual_calories += int(line)

    total_calories.sort(reverse = True)
    print("PART TWO total calories top 3: ", str(total_calories[0] + total_calories[1] + total_calories[2]))


if __name__ == "__main__":
    part_one()
    part_two()