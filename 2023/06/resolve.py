# -*- coding: utf-8 -*-
TIME = [40, 81, 77, 72] # test [7, 15, 30]
DISTANCE = [219, 1012, 1365, 1089] # test [9, 40, 200]

def get_ways_per_race(limit_time, limit_distance):
    ways = 0
    for hold_button in range(1, limit_time + 1):
        vel = limit_time - (limit_time - hold_button)
        distance = vel * (limit_time - hold_button)
        if distance > limit_distance:
            ways += 1
    return ways


def part_one():
    ways = 1
    for race in range(0, len(TIME)):
        ways *= get_ways_per_race(TIME[race], DISTANCE[race])
    print("PART ONE ways:", ways)

def part_two():
    time = int("".join(str(item) for item in TIME))
    distance = int("".join(str(item) for item in DISTANCE))
    print("PART TWO ways:", get_ways_per_race(time, distance))


if __name__ == "__main__":
    part_one()
    part_two()