# -*- coding: utf-8 -*-
import math
# F -> front
# B -> back
# L -> left
# R -> right
# F -> lower half
# B -> upper half
# R -> upper half 4-7
# L -> lower half 0-3
# FBFBBFFRLR -> last 3 characters specify exactly one of the 8 columns of seats on the plane

DATA_FILE='data.in'
TOTAL_COLUMNS=8
ROWS=range(0,128)
COLUMNS=range(0,8)

def read_file():
    f = open(DATA_FILE, "r")
    return f.readlines()

def lower_half(d):
    return d[0:len(d)/2]

def upper_half(d):
    return d[len(d)/2:]

def get_row(data):
    rw=ROWS
    for d in data:
        if d == 'F':
            rw=lower_half(rw)
        else: # B
            rw=upper_half(rw)
    return rw[0]

def get_column(data):
    cl=COLUMNS
    for d in data:
        if d=='R':
            cl=upper_half(cl)
        else: # B
            cl=lower_half(cl)
    return cl[0]

def get_seat_id(row, seat):
    return row * TOTAL_COLUMNS + seat

def problem_one():
    lines = read_file()
    result = 0
    for l in lines:
        line=l.replace('\n','')
        row=get_row(line[0:7])
        column=get_column(line[7:10])
        seat_id=get_seat_id(row, column)
        if seat_id > result:
            result = seat_id
    print("p1: "+ str(result))

def problem_two():
    lines = read_file()
    seats = []
    for l in lines:
        line=l.replace('\n','')
        row=get_row(line[0:7])
        column=get_column(line[7:10])
        seat_id=get_seat_id(row, column)
        seats.append(seat_id)
    seats.sort()
    i=seats[0]
    for s in seats:
        if s!=i: # break order, previously id is ok
            result=s-1
            break
        i=i+1
    print("p2: "+ str(result))


if __name__ == "__main__":
    problem_one()
    problem_two()
