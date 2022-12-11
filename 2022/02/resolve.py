# -*- coding: utf-8 -*-
DATA_FILE='data.in'
# A,X for Rock, B,Y for Paper, and C,Z for Scissors
# 1 for Rock, 2 for Paper, and 3 for Scissors
PLAYER_1_SCORES = {'A': 1, 'B': 2, 'C': 3}
PLAYER_2_SCORES = {'X': 1, 'Y': 2, 'Z': 3}
WIN = 6
DRAW = 3
LOSE = 0

def read_file():
    f = open(DATA_FILE, "r")
    return f.readlines()

def get_shape(line):
    result = line.replace('\n', '').split(' ')
    return result[0], result[1]

def scores(line):
    result = line.replace('\n', '').split(' ')
    return PLAYER_1_SCORES[result[0]], PLAYER_2_SCORES[result[1]]

def game_result(score_1, score_2):
    result = None
    if score_1 == score_2:
        result = DRAW
    elif abs(score_1-score_2) == 1:
        result = WIN if score_2 > score_1 else LOSE
    else:
        result = LOSE if score_2 > score_1 else WIN
    return score_2 + result

def game_result_two(shape_2, score_1, score_2):
    result = None
    if shape_2 == 'Y':
        result = score_1 + DRAW
    elif shape_2 == 'X':
        my_score = 3 if score_1 == 1 else (score_1 - 1)
        result = my_score + LOSE
    else: # Z
        my_score = 1 if score_1 == 3 else (score_1 + 1)
        result = my_score + WIN
    return result

def part_one():
    lines = read_file()
    total_score = 0
    i = 0
    for line in lines:
        player_1, player_2_me = scores(line)
        score_round = game_result(player_1, player_2_me)
        total_score += score_round
    print("PART ONE total score: ", str(total_score))

def part_two():
    lines = read_file()
    total_score = 0
    i = 0
    for line in lines:
        player_1, player_2_me = scores(line)
        player_1_shape, player_2_shape_me = get_shape(line)
        score_round = game_result_two(player_2_shape_me, player_1, player_2_me)
        total_score += score_round
    print("PART TWO total score: ", str(total_score))


if __name__ == "__main__":
    part_one()
    part_two()