# -*- coding: utf-8 -*-
DATA_FILE='data.in'

def read_file():
    f = open(DATA_FILE, "r")
    return f.readlines()

def file_to_arr(lines):
    arr = []
    for l in lines:
        arr.append(l.replace('\n', ''))
    return arr

#2427 NO
def get_value_before_second_time(instructions):
    index_executed=[]
    accumulator=0
    i=0
    while i not in index_executed:
        index_executed.append(i)
        inst, value = instructions[i].split(" ")
        inst_value = int(value[1:])
        if inst == 'acc':
            if value[0] == '+':
                accumulator += inst_value
            elif value[0] == '-':
                accumulator -= inst_value
            i = i + 1
        elif inst == 'nop':
            i = i + 1
        elif inst == 'jmp':
            if value[0] == '+':
                i += inst_value
            elif value[0] == '-':
                i -= inst_value
    return accumulator

def problem_one():
    lines = read_file()
    arr=file_to_arr(lines)
    acumulator=get_value_before_second_time(arr)

    print("p1: "+ str(acumulator))


if __name__ == "__main__":
    problem_one()
