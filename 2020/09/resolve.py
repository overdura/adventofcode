# -*- coding: utf-8 -*-
DATA_FILE='data.in'

PREAMBLE=25

def read_file():
    f = open(DATA_FILE, "r")
    return f.readlines()

def file_to_arr(lines):
    arr = []
    for l in lines:
        arr.append(int(l.replace('\n', '')))
    return arr

def is_arr_preamble_neq_value(arr_preamble, val):
    result = True
    i = 0
    for i in range(0, len(arr_preamble)-1):
        for a in range(i, len(arr_preamble)-1):
            if val == (arr_preamble[i]+arr_preamble[a+1]):
                result = False
                break
        if not result:
            break
        i+=1
    return result

def get_number_not_valid(xmas):
    result = None
    i = 0
    for a in range(PREAMBLE+1, len(xmas)):
        if is_arr_preamble_neq_value(xmas[i:a], xmas[a]):
            result = xmas[a]
            break
        i+=1
    return result


def problem_one():
    lines = read_file()
    arr=file_to_arr(lines)
    result=get_number_not_valid(arr)
    print("p1: "+ str(result))



if __name__ == "__main__":
    problem_one()
