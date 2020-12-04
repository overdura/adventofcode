# -*- coding: utf-8 -*-

DATA_FILE='data.in'
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

FIELDS_PASSPORT = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

def read_file():
    f = open(DATA_FILE, "r")
    return f.readlines()

def is_valid(passport):
    keys=[]
    for l in passport:
        if l in FIELDS_PASSPORT:
            keys.append(l)
    return True if (len(keys) == 8 and 'cid' in keys) or (len(keys) == 7 and 'cid' not in keys) else False

def problem_one():
    lines = read_file()
    total = 0
    passport = {}
    for l in lines:
        line=l.replace('\n', '')
        if line.strip()=='':
            if is_valid(passport):
                total=total+1
            passport={}
        else:
            passport_spc= line.split(' ')
            for p in passport_spc:
                k, v = p.split(":")
                passport[k]=v
    if is_valid(passport): #lastline
        total=total+1
    print(total)


if __name__ == "__main__":
    problem_one()
