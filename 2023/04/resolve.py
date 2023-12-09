# -*- coding: utf-8 -*-
DATA_FILE = 'data.in'

def read_file():
    f = open(DATA_FILE, "r")
    return f.readlines()

def winning_numbers(line):
    data = line.split(": ")[1].split(" | ")[0]
    result = []
    for item in data.split(" "):
        if item.isdigit():
            result.append(int(item))
    return result

def my_numbers(line):
    data = line.split(" | ")[1]
    result = []
    for item in data.split(" "):
        if item.strip().isdigit():
            result.append(int(item))
    return result

def calculate_points(arr):
    if len(arr) == 0:
        return 0
    i = 0
    result = 1
    while i <= len(arr):
        if i > 1:
            result = result * 2
        i+=1
    return result

def get_points(line):
    winner = winning_numbers(line)
    my = my_numbers(line)
    result = set()
    for item in my:
        if item in winner:
            result.add(item)
    return calculate_points(result)

def part_one():
    lines = read_file()
    total_points = 0
    for line in lines:
        total_points += get_points(line)
    print("PART ONE total points:", total_points)

def part_two():
    lines = read_file()
    scratchcards = 0
    print("PART TWO total scratchcards:", scratchcards)


if __name__ == "__main__":
    part_one()
    #part_two()