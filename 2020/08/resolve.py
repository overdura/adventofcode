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

def assign_accumulator_and_i(inst, value, inst_value, accumulator, i):
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
    return accumulator, i


def get_repeat_index_instructions(instructions):
    index_executed=[]
    accumulator=0
    i=0
    while i not in index_executed:
        index_executed.append(i)
        inst, value = instructions[i].split(" ")
        inst_value = int(value[1:])
        accumulator, i=assign_accumulator_and_i(inst, value, inst_value, accumulator, i)
    return index_executed

def replace_instruction_before_second_time(instructions, index_executed):
    ex=0
    accumulator=0
    j=1
    while ex<len(instructions):
        idx_ex=[]
        i=0
        accumulator=0
        while i not in idx_ex:
            if i>=len(instructions):
                break
            idx_ex.append(i)
            inst, value = instructions[i].split(" ")
            inst_value = int(value[1:])
            accumulator, i=assign_accumulator_and_i(inst, value, inst_value, accumulator, i)
        ex = i
        inst_c=None
        err_idx=0
        for r in range(len(index_executed)-j, 0, -1): # last no count
            err_idx=index_executed[r]
            inst_c, val=instructions[err_idx].split(" ")
            if inst_c in ['jmp', 'nop']:
                inst_c = 'nop' if inst_c =='jmp' else 'jmp'
                break
        instructions[err_idx] = inst_c+" "+val # change nop -> jmp or jmp -> nop
        j+=1
    return accumulator


def problem_one():
    lines = read_file()
    instructions=file_to_arr(lines)
    acumulator=get_value_before_second_time(instructions)
    print("p1: "+ str(acumulator))

def problem_two():
    lines = read_file()
    instructions=file_to_arr(lines)
    # get index previous second time
    index_not_repeated=get_repeat_index_instructions(instructions)
    # for last to init [index_not_repeated] change jmp->nop or nop->jmp and check if finish instructions
    accumulator=replace_instruction_before_second_time(instructions, index_not_repeated)
    print("p2: "+ str(accumulator))


if __name__ == "__main__":
    problem_one()
    problem_two()
