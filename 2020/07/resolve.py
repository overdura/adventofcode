# -*- coding: utf-8 -*-
DATA_FILE='data.in'

KEY="shiny gold"

def read_file():
    f = open(DATA_FILE, "r")
    return f.readlines()

# get all bags with bags inside
def get_rosetta_bag(lines):
    rosetta={}
    for l in lines:
        line = l.replace('\n', '').replace(' bags', '-').replace(' bag', '-').replace('.', '').replace(',', '').replace('contain', '')
        bags_colors=line.split('-')
        key=bags_colors[0]
        values=[]
        for i in range(1, len(bags_colors)):
            vb = bags_colors[i].strip()
            if vb != '':
                values.append(vb[0]+'-'+vb[2:])
        rosetta[key]=values
    return rosetta

# only count one bag KEY (shiny gold)
def count_one_key_bags_out(key_group, rosetta):
    result = 0
    if key_group==KEY:
        result = 1
    else:
        if key_group not in rosetta:
            result = 0
        else:
            for e in rosetta[key_group]:
                result = result + count_one_key_bags_out(e.split('-')[1], rosetta)
                if result > 0:
                    break
    return result if result == 0 else 1

# individual bags are inside KEY (shiny gold)
def recursive_count_individual_bags_for_key(key_group, rosetta, amount):
    result = 0
    for e in rosetta[key_group]:
        key_name=e.split('-')[1]
        num = int(e.split('-')[0]) if e.split('-')[0] !='n' else 1
        if key_name in rosetta:
            result += num + recursive_count_individual_bags_for_key(key_name, rosetta, num)
    return amount * result


def problem_one():
    result=0
    lines = read_file()
    rosetta_bags=get_rosetta_bag(lines)
    for l in lines:
        line = l.replace('\n', '').replace(' bags', '-').replace(' bag', '-').replace('.', '').replace(',', '').replace('contain', '')
        bags_colors=line.split('-')
        bag_out=bags_colors[0]
        if bag_out != KEY:
            result=result+count_one_key_bags_out(bag_out, rosetta_bags)
    print("p1: "+ str(result))


def problem_two():
    result=0
    lines = read_file()
    rosetta_bags=get_rosetta_bag(lines)
    for r in rosetta_bags:
        if r == KEY:
            result+= recursive_count_individual_bags_for_key(r, rosetta_bags,1)
    print("p2: "+ str(result))


if __name__ == "__main__":
    problem_one()
    problem_two()
