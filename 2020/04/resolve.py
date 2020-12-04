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

# part two
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
## If cm, the number must be at least 150 and at most 193.
## If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

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

def is_valid_problem_two(passport):
    keys=[]
    for l, v in passport.items():
        if l in FIELDS_PASSPORT:
            ok=False
            if l=='byr' and int(v)>=1920 and int(v)<=2002:
                ok=True
            if l=='iyr' and int(v)>=2010 and int(v)<=2020:
                ok=True
            if l=='eyr' and int(v)>=2020 and int(v)<=2030:
                ok=True
            if l=='hgt':
                val_no_txt=v.replace('cm','').replace('in','')
                if ('cm' in v and int(val_no_txt)>=150 and int(val_no_txt)<=193) or 'in' in v and int(val_no_txt)>=59 and int(val_no_txt)<=76:
                    ok=True
            if l=='hcl' and len(v)==7:
                ok=True
            if l=='ecl' and v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                ok=True
            if l=='pid' and len(v)==9:
                ok=True
            if ok:
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
    print("p1: "+ str(total))

def problem_two():
    lines = read_file()
    total = 0
    passport = {}
    for l in lines:
        line=l.replace('\n', '')
        if line.strip()=='':
            if is_valid_problem_two(passport):
                total=total+1
            passport={}
        else:
            passport_spc= line.split(' ')
            for p in passport_spc:
                k, v = p.split(":")
                passport[k]=v
    if is_valid_problem_two(passport): #lastline
        total=total+1
    print("p2: "+ str(total))


if __name__ == "__main__":
    problem_one()
    problem_two()
