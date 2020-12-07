# -*- coding: utf-8 -*-
DATA_FILE='data.in'

KEY="shiny gold"

def read_file():
    f = open(DATA_FILE, "r")
    return f.readlines()

# get all bags with bags in
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

def count_key_bags_out(k, rosetta):
    key_count=k.split('-')[1]
    if key_count==KEY:
        return 1
    else:
        if key_count in rosetta:
            for kk in rosetta[key_count]:
                return count_key_bags_out(kk, rosetta)
        else:
            return 0

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


if __name__ == "__main__":
    problem_one()
