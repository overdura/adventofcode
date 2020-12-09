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

def get_encryption_weakness(invalid_number, xmas):
    first_element_idx=None
    last_element_idx=None
    for i in range(0, len(xmas)):
        first_element_idx=i
        accum=xmas[i]
        for j in range(i+1, len(xmas)):
            last_element_idx=j
            accum+=xmas[j]
            if accum == invalid_number:
                break
        else:
            continue
        break
    contiguous=xmas[first_element_idx:last_element_idx+1]
    contiguous.sort()
    return contiguous[0]+contiguous[len(contiguous)-1]

def problem_one():
    lines = read_file()
    arr=file_to_arr(lines)
    result=get_number_not_valid(arr)
    print("p1: "+ str(result))

def problem_two():
    lines = read_file()
    arr=file_to_arr(lines)
    invalid_number=get_number_not_valid(arr)
    encryption_weakness=get_encryption_weakness(invalid_number, arr[0:arr.index(invalid_number)])
    print("p2: "+ str(encryption_weakness))

if __name__ == "__main__":
    problem_one()
    problem_two()
