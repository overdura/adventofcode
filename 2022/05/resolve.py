# -*- coding: utf-8 -*-
DATA_FILE='data.in'

def read_file():
    f = open(DATA_FILE, "r")
    return f.readlines()

def clean_line(line):
    return line.replace('\n', '')
    
def clean_stacks_line(line):
    line = clean_line(line)
    line = line.replace('[',' ').replace(']',' ').replace('   ', '')
    return line[1:].rstrip()

def get_number_stacks(lines):
    for line in lines:
        find_digit = clean_line(line).split(' ')
        for n in find_digit[::-1]:
            if n.strip().isdigit():
                return int(n.strip())

def get_crates(line):
    return [c.strip() for c in line]

def fill_stacks(stacks, crates):
    i = 0
    for crate in crates:
        stacks[i] = crate+stacks[i]
        i += 1

def get_stacks(lines):
    total_columns = get_number_stacks(lines)
    stacks = ['' for i in range(0, total_columns)]
    for line in lines:
        line = clean_stacks_line(line)
        finisher = line.replace(' ','')
        if finisher.isdigit():
            break
        crates = get_crates(line)
        fill_stacks(stacks, crates)
    return stacks

def get_movements(lines):
    # elements - source - target
    movements = []
    for line in lines:
        line = clean_line(line)
        if ('move' in line):
            elements = line.split('move ')[1][0:2].strip()
            source = line.split('from ')[1][0:2].strip()
            target = line.split('to ')[1][0:2].strip()
            movements.append(elements+'-'+source+'-'+target)
    return movements

def move(stacks, movement, reverse):
    elements = int(movement[0])
    source = int(movement[1])-1
    target = int(movement[2])-1
    total_len_source = len(stacks[source])
    ini_elements = total_len_source-elements 
    elements_to_move = stacks[source][ini_elements:total_len_source]
    stacks[source] = stacks[source][0:total_len_source-len(elements_to_move)]
    elements_to_move_ordered = elements_to_move[::-1] if reverse else elements_to_move
    stacks[target] += elements_to_move_ordered

def move_crates(stacks, movements, reverse):
    for m in movements:
        movement = m.split('-')
        move(stacks, movement, reverse)

def get_top_stacks(stacks):
    top_stacks = ''
    for el in stacks:
        top_stacks += el[len(el)-1]
    return top_stacks

def resolve(reverse):
    lines = read_file()
    stacks = get_stacks(lines)
    movements = get_movements(lines)
    move_crates(stacks, movements, reverse)
    return get_top_stacks(stacks)

def part_one():
    print("PART ONE crates: ", resolve(True)) # JDTMRWCQJ

def part_two():
    print("PART TWO crates: ", resolve(False)) # VHJDDCWRD


if __name__ == "__main__":
    part_one()
    part_two()