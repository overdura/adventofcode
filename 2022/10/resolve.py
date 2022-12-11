# -*- coding: utf-8 -*-
DATA_FILE='data.in'

def read_file():
    f = open(DATA_FILE, "r")
    return f.readlines()

def clean_line(line):
    return line.replace('\n', '')

def get_instruction(line):
    return line.split(' ')
    
def instruction_cycles(instruction):
    return len(instruction)

def get_signal_strengths():
    signal_strengths = []
    x = 1
    cycle = 0
    signal_strength = 20
    for line in read_file():
        instruction = get_instruction(clean_line(line))
        cycle += instruction_cycles(instruction)

        if (cycle >= signal_strength):
            signal_strengths.append(signal_strength * x)
            signal_strength += 40

        if instruction[0] == 'addx':
            x += int(instruction[1])

    return signal_strengths

def get_sum_signal_strengths(signal_strengths):
    sum_signal_strengths = 0
    for s in signal_strengths:
        sum_signal_strengths += s 
    return sum_signal_strengths

def print_crt(crt):
    for i in range(len(crt)):
        print(crt[i])

def get_cycle_positions():
    result = {}
    cycle = 0
    x = 1
    for line in read_file(): 
        instruction = get_instruction(clean_line(line))
        cycle += instruction_cycles(instruction)
        if instruction[0] == 'addx':
            x += int(instruction[1])
            result[cycle] = x
    return result

def match_pixel_sprite(pixel, sprite):
    return pixel in [sprite, sprite+1, sprite+2]

def create_crt():
    crt = []
    cycle_positions = get_cycle_positions()
    crt_line = ''
    current_pixel = 0
    current_sprite = 0
    
    for cycle in range(0, 241):
        if (cycle % 40 == 0):
            crt.append(crt_line)
            crt_line = ''
            current_pixel = 0
            current_sprite = 0

        if cycle in cycle_positions.keys():
            current_sprite = cycle_positions[cycle]-1

        crt_line += '#' if match_pixel_sprite(current_pixel, current_sprite) else '.'

        current_pixel += 1

    return crt

def part_one():
    signal_strengths = get_signal_strengths()
    sum_signal_strengths = get_sum_signal_strengths (signal_strengths)
    print("PART ONE sum signal strengths: ", sum_signal_strengths)

def part_two():
    crt = create_crt()
    print("PART TWO:")
    print_crt(crt) 


if __name__ == "__main__":
    part_one()
    part_two()