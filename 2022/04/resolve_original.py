# -*- coding: utf-8 -*-
DATA_FILE='data.in'

def read_file():
    f = open(DATA_FILE, "r")
    return f.readlines()

def clean_line(line):
    return line.replace('\n', '').strip()

def get_sections(line):
    sections = clean_line(line).split(',')
    return sections[0], sections[1]

def get_min_max_section(section):
    min_max = section.split('-')
    return int(min_max[0]), int(min_max[1])

def is_section_contained_in_other(section_1, section_2):
    min_section_1, max_section_1 = get_min_max_section(section_1)
    min_section_2, max_section_2 = get_min_max_section(section_2)
    return min_section_1 >= min_section_2 and max_section_1 <= max_section_2

def is_section_overlap(section_1, section_2):
    min_section_1, max_section_1 = get_min_max_section(section_1)
    min_section_2, max_section_2 = get_min_max_section(section_2)
    return max_section_1 >= min_section_2 and max_section_1 <= max_section_2

def is_contained(section_1, section_2):
    result = False

    if (is_section_contained_in_other(section_1, section_2) or \
        is_section_contained_in_other(section_2, section_1)):
       result = True


    return result

def is_overlap(section_1, section_2):
    result = False
    if (is_section_overlap(section_1, section_2) or \
        is_section_overlap(section_2, section_1)):
       result = True

    return result

def part_one():
    lines = read_file()
    total_pairs_contained = 0
    for line in lines:
        section_1, section_2 = get_sections(line)
        contained = is_contained(section_1, section_2)
        if (contained):
            total_pairs_contained += 1

    print("PART ONE pairs contained in other: ", str(total_pairs_contained))

def part_two():
    lines = read_file()
    total_overlap = 0
    for line in lines:
        section_1, section_2 = get_sections(line)
        overlap = is_overlap(section_1, section_2)
        if (overlap):
            total_overlap += 1

    print("PART TWO pairs overlap: ", str(total_overlap))


if __name__ == "__main__":
    part_one()
    part_two()