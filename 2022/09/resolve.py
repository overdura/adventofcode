# -*- coding: utf-8 -*-
DATA_FILE='data.in'

def read_file():
    f = open(DATA_FILE, "r")
    return f.read().splitlines()

def get_instruction(line):
    result = line.split(' ')
    return result[0], int(result[1])

def add_positions(positions, x, y):
    position = str(x) + '|' + str(y)
    #print("add_pos:", x, y)
    positions.append(position) 

def clean_repeated_position(positions):
    result = []
    for position in positions[1:]: # init position skipped
        if  position not in result:
            result.append(position)
    return result

def get_position(positions):
    result = positions.split('|')
    return int(result[0]), int(result[1])

def calculate_tail_positions():
    #0,2 1,2 2,2
    #0,1 1,1 2,1
    #0,0 1,0 2,0
    head_positions = ['0|0']
    tail_positions = []
    last_head_position = ''
    head_x = 0
    head_y = 0
    tail_x = 0
    tail_y = 0
    tail_positions=['0|0']

    for line in read_file():
        #last_head_position = (str(head_x) + '|' + str(head_y))
        #head_x, head_y = last_position(last_head_position)
        #last_head_position = head_positions[len(head_positions)-1]
        #head_x, head_y = get_position(last_head_position)
        #print("\nlast_head:", head_x, head_y, last_head_position)

        direction, step = get_instruction(line)
        print(direction+str(step))
        for s in range(0, step):
            if direction == 'R':
                head_x += 1
            elif direction == 'L':
                head_x -= 1
            elif direction == 'U':
                head_y += 1
            elif direction == 'D':
                head_y -= 1
    
            print("step:", s, head_x, head_y)
            #position = str(head_x) + '|' + str(head_y)
            #head_positions.append(position)
            diff_x = head_x - tail_x
            diff_y = head_y - tail_y
            not_touching = abs(diff_x) > 1 or abs(diff_y) > 1

            print("diff:", s, diff_x, diff_y, not_touching)
            
            if not_touching:
                print((0 if diff_x == 0 else diff_x // abs(diff_x)))
                print((0 if diff_y == 0 else diff_y // abs(diff_y)))
                x = (0 if diff_x == 0 else diff_x // abs(diff_x))
                y = (0 if diff_y == 0 else diff_y // abs(diff_y))
                tail_x += x
                tail_y += y
                position = str(tail_x) + '|' + str(tail_y)
                if position not in tail_positions:
                    tail_positions.append(position)
            #    position = str(head_x) + '|' + str(head_y)
            #    if position not in tail_positions:
            #        tail_positions.append(position)
        
            
        '''diff_x = head_x - tail_x
            diff_y = head_y - tail_y
            print("diff:", s, diff_x, diff_y)

            not_touching = abs(diff_x) > 0 or abs(diff_y) > 0

            if not_touching:
                print("add tail", diff_x, diff_y)
                #tail_x += abs(diff_x);
                #tail_y += abs(diff_y);
                position = str(head_x) + '|' + str(head_y)
                if position not in tail_positions:
                    tail_positions.append(position)

            '''
        '''

        if direction == 'R':
            ini = head_x + 1
            end = (ini + step)
            print(ini, end)
            for x in range(ini, end):
                head_x = x
                #print("x,y: ", head_x, head_y)
                add_positions(head_positions, head_x, head_y)
                #tail = head_positions[len(head_positions)-2]
                #tail_x, tail_y = get_position(tail)
                #print('tail', tail_x, tail_y)
                add_positions(tail_positions, head_x-1, head_y)

        elif direction == 'L':
            ini = head_x - 1
            end = ini - step
            #print(ini, end)
            for x in range(ini, end, -1):
                head_x = x
                #print("x,y: ", head_x, head_y)
                add_positions(head_positions, head_x, head_y)

        elif direction == 'U':
            ini = head_y + 1
            end = ini + step
            print(ini, end)
            for y in range(ini, end):
                head_y = y
                #print("x,y: ",  head_x, head_y)
                add_positions(head_positions, head_x, head_y)
                tail = head_positions[len(head_positions)-1]
                tail_x, tail_y = get_position(tail)
                print(tail, abs(head_x-tail_x))
            break
                #tail = head_positions[len(head_positions)-2]
                #print(tail)
                #add_positions(tail_positions, head_x, head_y-1)

                #print("check", head_x, head_y, tail_x, tail_y)

                #tail = head_positions[len(head_positions)-1]
                #tail_x, tail_y = get_position(tail)
                #add_positions(tail_positions, tail_x, tail_y)
            #break

        elif direction == 'D':
            ini = head_y - 1
            end = ini - step
            print(ini, end)
            for y in range(ini, end, -1):
                head_y = y
                #print("x,y: ", head_x, head_y)
                add_positions(head_positions, head_x, head_y)
                #tail = head_positions[len(head_positions)-3]
                #tail_x, tail_y = get_position(tail)
                #print('tail', tail_x, tail_y)
                #add_positions(tail_positions, tail_x, tail_y)
        '''

    #print('head:', len(head_positions), head_positions)
    #-> HEAD
    #-> .HHHH.
    #-> .HHHHH
    #-> HHHHHH
    #-> ....H.
    #-> sHHHH.
    head_cleaned_positions = clean_repeated_position(head_positions)
    tail_cleaned_positions = clean_repeated_position(tail_positions)

    print(len(head_positions), 'head', head_positions)
    print('*', len(head_cleaned_positions), 'head clean', head_cleaned_positions)
    print(len(tail_positions), 'tail', tail_positions)
    print('*', len(tail_cleaned_positions), 'tail clean', tail_cleaned_positions)

    return len(tail_cleaned_positions)

def part_one():
    positions = calculate_tail_positions()
    print("PART ONE positions: ", positions)

def part_two():
    positions = 0
    print("PART TWO positions: ", positions) 

if __name__ == "__main__":
    part_one()
    part_two()
