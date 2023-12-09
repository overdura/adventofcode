# -*- coding: utf-8 -*-
DATA_FILE = 'data.in'

def read_file():
    f = open(DATA_FILE, "r")
    return f.readlines()

def check_element_is_symbol(elements):
    for element in elements:
        if not element.isdigit() and element not in [".", "\n"]:
            return True
    return False

def is_part_engine(ini_column, end_column, line, prev_line, post_line):
    elements = []
    if ini_column-1 > 0:
        elements.append(line[ini_column-1])
    if (end_column+1) < len(line):
        elements.append(line[end_column+1])
    if prev_line != None:
        elements.extend(prev_line[ini_column:end_column+1])
        if ini_column-1 > 0:
            elements.append(prev_line[ini_column-1])
        if (end_column+1) < len(line):
            elements.append(prev_line[end_column+1])
    if post_line != None:
        elements.extend(post_line[ini_column:end_column+1])
        if ini_column-1 > 0:
            elements.append(post_line[ini_column-1])
        if (end_column+1) < len(line):
            elements.append(post_line[end_column+1])
    return check_element_is_symbol(elements)

def sum_part_engine(line, prev_line, post_line):
    sum_part_engine = 0
    current_column = 0
    number_to_check = ""
    for item in line:
        if item.isdigit():
            number_to_check += item
        else:
            if number_to_check != "" and is_part_engine((current_column-1)-(len(number_to_check)-1), current_column-1, line, prev_line, post_line):
                sum_part_engine += int(number_to_check)
            number_to_check = ""
        current_column += 1
    return sum_part_engine

def get_number(line, column):
    result = ""
    for item in line[column:]:
        if item.isdigit():
            result += item
        else:
            return int(result)
    return result

def fill_engine_schematic():
    lines = read_file()
    return [[item for item in line] for line in lines]


def part_one():
    engine_schematic = fill_engine_schematic()
    sum_parts_engine = 0
    current_line = 0
    for line in engine_schematic:
        prev_line = engine_schematic[current_line-1] if current_line>1 else None
        post_line = engine_schematic[current_line+1] if current_line<len(engine_schematic)-1 else None
        sum_parts_engine += sum_part_engine(line, prev_line, post_line)
        current_line += 1
    print("PART ONE sum part numbers engine:", sum_parts_engine)

def part_two():
    engine_schematic = fill_engine_schematic()
    sum_gear_ratios = 0
    print("TWO ONE sum part numbers engine:", sum_gear_ratios)


if __name__ == "__main__":
    part_one()
    part_two()