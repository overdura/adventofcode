# -*- coding: utf-8 -*-
DATA=[7,12,1,0,16,2]
END_TURN_1=2020
END_TURN_2=30000000

def get_age(arr, last_number):
    result=[]
    for i in range(len(arr)-1, -1, -1):
        if arr[i]==last_number:
            result.append(i+1)
        if len(result) == 2:
            break
    return result[0]-result[1]

def problem(data, end_turn):
    init_numbers=data[:]
    # number:[ix_1, ix_2, ix_3]
    spoken_numbers={}
    turn=1
    last_number = None
    for n in init_numbers:
        spoken_numbers[n]=[turn]
        last_number=n
        turn+=1
    while turn <= end_turn:
        if last_number in spoken_numbers and len(spoken_numbers[last_number])==1:
            arr=spoken_numbers[0]
            arr.append(turn)
            if len(arr)>2:
                spoken_numbers[0]=arr[1:]
            else:
                spoken_numbers[0]=arr
            last_number=0
        else:
            arr=spoken_numbers[last_number]
            last_number=arr[-1]-arr[-2]
            arr_ln=[turn]
            if last_number in spoken_numbers:
                arr_ln = spoken_numbers[last_number]
                arr_ln.append(turn)
            spoken_numbers[last_number]=arr_ln
        turn+=1
    result = "p1: " if end_turn == END_TURN_1 else "p2: "
    print(result+ str(last_number))

if __name__ == "__main__":
    problem(DATA, END_TURN_1)
    problem(DATA, END_TURN_2)
