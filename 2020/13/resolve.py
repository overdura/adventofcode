# -*- coding: utf-8 -*-
DATA_FILE='data.in'

def read_file():
    f = open(DATA_FILE, "r")
    return f.readlines()

def get_buses(lines):
    b=[]
    for l in lines.split(','):
        if l != 'x':
            b.append(l)
    return b

def get_ts_next_buses(ts, buses):
    result={}
    for b in buses:
        ini=0
        bus=int(b)
        while ini <= ts:
            ini+=bus
        result[b]=ini
    return result

def get_my_bus_earliest_x_minutes(ts, buses):
    result=None
    diff=None
    for b, t in buses.items():
        if diff==None or diff > int(t)-int(ts):
            diff=int(t)-int(ts)
            result=int(b)*diff
    return result

def problem_one():
    lines=read_file()
    current_ts=int(lines[0].replace('\n',''))
    buses=get_buses(lines[1].replace('\n',''))
    earliest_timetable=get_ts_next_buses(current_ts, buses)
    earliest_x_minutes=get_my_bus_earliest_x_minutes(current_ts, earliest_timetable)
    print("p1: "+ str(earliest_x_minutes))


if __name__ == "__main__":
    problem_one()
