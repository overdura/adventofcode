# -*- coding: utf-8 -*-
DATA_FILE='data.in'

LOWER_LETTERS = [chr(i) for i in range(97, 123)]
UPPER_LETTERS = [l.upper() for l in LOWER_LETTERS]
ALPHABET = LOWER_LETTERS + UPPER_LETTERS

#PART ONE priorities:  8109
#PART TWO priorities:  2738

def read_file():
    f = open(DATA_FILE, "r")
    return f.readlines()

def clean_line(line):
    return line.replace('\n', '').strip()

def get_compartments(line):
    total_elements = len(line)
    half_elements = round(total_elements / 2)
    compartment_1 = line[0 : half_elements]
    compartment_2 = line[half_elements : total_elements]
    return compartment_1, compartment_2

def get_common_element(comparment_1, comparment_2):
    result = None
    for c1 in comparment_1:
        for c2 in comparment_2:
            if c1 == c2:
                return c1 
    return result

'''def get_common_element_3(comparment_1, comparment_2, comparment_3):
    result = None
    for c1 in comparment_1:
        for c2 in comparment_2:
            common = None 
            if c1 == c2:
                common = c2
            for c3 in comparment_3:
                if common == c3:
                    return c3 
    return result 
'''

def get_common_element_3(group):
    common_element = None
    group_0 = group[0]
    group_1 = group[1]

    exclude_elements = []
    while(common_element == None):
        common_element_1_2 = get_common_element(group_0, group_1)
        common_element = get_common_element([common_element_1_2], group[2])
        if common_element != None:
            return common_element

        group_0 = group_0.replace(common_element_1_2, '')
        group_1 = group_1.replace(common_element_1_2, '')

    return common_element

def get_priority(element):
    return ALPHABET.index(element) + 1

def part_one():
    lines = read_file()
    total_priorities = 0
    for line in lines:
        compartment_1, compartment_2 = get_compartments(clean_line(line))
        common_element = get_common_element(compartment_1, compartment_2)
        element_priority = get_priority(common_element)
        total_priorities += element_priority
    print("PART ONE priorities: ", str(total_priorities))

def part_two():
    lines = read_file()
    total_priorities = 0
    group = []
    for line in lines:
        group.append(clean_line(line))
        if len(group) == 3:
            common_element = get_common_element_3(group)
            #common_element = get_common_element_3(group[0], group[1], group[2])
            element_priority = get_priority(common_element)
            total_priorities += element_priority
            group = []
    print("PART TWO priorities: ", str(total_priorities))


if __name__ == "__main__":
    part_one()
    part_two()