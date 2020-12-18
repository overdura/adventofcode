# -*- coding: utf-8 -*-
DATA_FILE='data.in'

YOUR_TICKET_TEXT="your ticket:"
NEARBY_TICKETS_TEXT="nearby tickets:"
def read_file():
    f = open(DATA_FILE, "r")
    return f.readlines()

def file_to_arr(lines):
    arr = []
    for l in lines:
        arr.append(l.replace('\n', ''))
    return arr

def get_ticket_fields(arr):
    result=[]
    for a in arr:
        if len(a)==0:
            break
        line = a.split(":")
        content=line[1].strip().split(" or ")
        result.append([line[0], content[0], content[1]])
    return result

def get_error_rate_line(ticket_fields, line):
    result=0
    i = 0
    while i < len(ticket_fields):
        val_to_check=int(line[i])
        result=val_to_check
        for tf in ticket_fields:
            tf_range_1 = tf[1].split("-")
            tf_range_2 = tf[2].split("-")
            if (val_to_check>=int(tf_range_1[0]) and val_to_check<=int(tf_range_1[1])) or (val_to_check>=int(tf_range_2[0]) and val_to_check<=int(tf_range_2[1])):
                result=0
        if result > 0:
            break
        i+=1
    return result


def problem_one():
    error_rate=0
    lines = read_file()
    arr = file_to_arr(lines)
    ticket_fields=get_ticket_fields(arr)
    nearby=False
    for a in arr:
        if nearby:
            values=a.split(",")
            error_rate+=get_error_rate_line(ticket_fields, values)
        if a==NEARBY_TICKETS_TEXT:
            nearby=True
    print("p1: "+str(error_rate))



if __name__ == "__main__":
    problem_one()
