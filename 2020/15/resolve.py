# -*- coding: utf-8 -*-
DATA=[7,12,1,0,16,2]
END_TURN=2020

def get_age(arr, last_number):
    result=[]
    for i in range(len(arr)-1, -1, -1):
        if arr[i]==last_number:
            result.append(i+1)
        if len(result) == 2:
            break
    return result[0]-result[1]

def problem_one():
    spoken_numbers=DATA
    turn=len(spoken_numbers)+1
    while turn <= END_TURN:
        last_number=spoken_numbers[-1]
        if spoken_numbers.count(last_number) == 1:
            spoken_numbers.append(0)
        else:
            spoken_numbers.append(get_age(spoken_numbers, last_number))
        turn+=1

    print("p1: "+ str(spoken_numbers[-1]))




if __name__ == "__main__":
    problem_one()
