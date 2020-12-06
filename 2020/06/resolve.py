# -*- coding: utf-8 -*-
import math

DATA_FILE='data.in'

def read_file():
    f = open(DATA_FILE, "r")
    return f.readlines()

def count_answers(line, group):
    for l in line:
        if l not in group:
            group.append(l)
    return group

def count_everyone_yes_answers(line, group):
    result = [];
    if len(group)==0:
        for l in line:
            result.append(l)
    else:
        gr = []
        for l in line:
            gr.append(l)
        result = list(set(group) & set(gr))
        if len(result)==0:
            result=['-']
    return result


def problem_one():
    lines = read_file()
    result = 0
    group=[]
    for l in lines:
        line=l.replace('\n','')
        if line != '':
            group=count_answers(line, group)
        else:
            result=result+len(group)
            group=[]
    result=result+len(group)
    print("p1: "+ str(result))

def problem_two():
    lines = read_file()
    result = 0
    group=[]
    for l in lines:
        line=l.replace('\n','')
        if line != '':
            group=count_everyone_yes_answers(line, group)
        else:
            if len(group)>0 and group[0]!='-':
                result=result+len(group)
            group=[]
    if len(group)>0 and group[0]!='-':
        result=result+len(group)
    print("p2: "+ str(result))


if __name__ == "__main__":
    problem_one()
    problem_two()
