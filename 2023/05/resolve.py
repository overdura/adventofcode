# -*- coding: utf-8 -*-
DATA_FILE = 'data.in'

def read_file():
    f = open(DATA_FILE, "r")
    return f.readlines()

def get_seeds():
    seeds = []
    lines = read_file()
    for line in lines:
        seeds = [int(item.strip()) for item in line.replace("seeds: ", "").split(" ")]
        break
    return seeds

def get_key(line):
    if "map:" in line:
        return line.split(" ")[0]
    return None

def get_seed_map():
    result = {}
    lines = read_file()
    i = 0
    key = None
    last_key = None
    for line in lines:
        if (i > 0):
            key = get_key(line)
            if (key != None):
                last_key = key
                result[key] = []
            elif line != "\n":
                items = line.replace("\n", "").split(" ")
                destination = int(items[0])
                source = int(items[1])
                end_range = int(items[2])
                result[last_key].append([source, destination, end_range])
        i += 1
    return result

def convert(key_start, key_end, seed, seed_map):
    current_key = key_start
    result = seed
    for key_map in seed_map:
        for value in seed_map[key_map]:
            if seed >= value[0] and seed <= value[0]+value[2]:
                result = (value[1]+value[2]) - (value[0]+value[2]-seed)
                seed = result
                break
        current_key = key_map.split("-to-")[1]
        if current_key == key_end:
            break
    return result

def part_one():
    seeds = get_seeds()
    seed_map = get_seed_map()
    result = []
    for seed in seeds:
        result.append(convert("seed", "location", seed, seed_map))
    result.sort()
    print("PART ONE location:", result[0])

'''def part_two():
    lines = read_file()
    print("PART TWO total")
'''

if __name__ == "__main__":
    part_one()
    #part_two()