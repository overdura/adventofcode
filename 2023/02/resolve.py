# -*- coding: utf-8 -*-
DATA_FILE = 'data.in'

MAX_RED_CUBES = 12
MAX_GREEN_CUBES = 13
MAX_BLUE_CUBES = 14

def read_file():
    f = open(DATA_FILE, "r")
    return f.readlines()

def get_number(data):
    return int(data.split(" ")[0]) 

def is_outside_limit(data, limit):
    return limit < data

def is_valid_values(data):
    values = data.split(", ")
    for value in values:
        if "red" in value:
            if is_outside_limit(get_number(value), MAX_RED_CUBES):
                return False
        elif "green" in value:
            if is_outside_limit(get_number(value), MAX_GREEN_CUBES):
                return False
        else: # blue
            if is_outside_limit(get_number(value), MAX_BLUE_CUBES):
                return False
    return True

def is_valid_game(data):
    shifts = data.split("; ")
    for shift in shifts:
        if not is_valid_values(shift):
            return False
    return True

def get_valid_game(line):
    game, data = line.split(': ')
    number_game = game.replace("Game ", "")
    if is_valid_game(data):
        return int(number_game)
    else:
        return 0

def get_max_value(value, previous_value):
    number_value = int(value.split(" ")[0])
    return number_value if number_value > previous_value else previous_value

def get_power_game(data):
    red = 0
    green = 0
    blue = 0
    cubes_group = data.split("; ")
    for cubes in cubes_group:
        for cube in cubes.split(", "):
            if "red" in cube:
                red = get_max_value(cube, red)
            elif "green" in cube:
                green = get_max_value(cube, green)
            else:
                blue = get_max_value(cube, blue)
    return red * green * blue


def part_one():
    lines = read_file()
    valid_games = 0
    for line in lines:
        valid_games += get_valid_game(line)
    print("PART ONE sum IDs:", valid_games)

def part_two():
    lines = read_file()
    sum_power = 0
    for line in lines:
        cubes = line.split(': ')[1]
        sum_power += get_power_game(cubes)
    print("PART TWO sum of the power:", sum_power)


if __name__ == "__main__":
    part_one()
    part_two()