# -*- coding: utf-8 -*-
DATA=[2, 49, 78, 116, 143, 42, 142, 87, 132, 86, 67, 44, 136, 82, 125, 1, 108, 123, 46, 37, 137, 148, 106, 121, 10, 64, 165, 17, 102, 156, 22, 117, 31, 38, 24, 69, 131, 144, 162, 63, 171, 153, 90, 9, 107, 79, 7, 55, 138, 34, 52, 77, 152, 3, 158, 100, 45, 129, 130, 135, 23, 93, 96, 103, 124, 95, 8, 62, 39, 118, 164, 172, 75, 122, 20, 145, 14, 112, 61, 43, 141, 30, 85, 101, 151, 29, 113, 94, 68, 58, 76, 97, 28, 111, 128, 21, 11, 163, 161, 4, 168, 157, 27, 72]

def problem_one():
    result = 0
    DATA.sort()
    one=[]
    three=[]
    i=0
    for d in DATA:
        if i < len(DATA)-1:
            if i == 0:
                if DATA[i]-0==1:
                    one.append(d)
                elif DATA[i+1]-DATA[i]==3:
                    three.append(d)
            if DATA[i+1]-DATA[i]==1:
                one.append(d)
            elif DATA[i+1]-DATA[i]==3:
                three.append(d)
        i+=1
    result=len(one)*(len(three)+1) # +1 last element *3
    print("p1: "+ str(result))


if __name__ == "__main__":
    problem_one()
