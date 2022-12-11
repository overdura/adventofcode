# -*- coding: utf-8 -*-
import math
import sys

DATA_FILE='data.in'

class Monkey:
    def __init__(self, items=[], operation=None, test=None, success=None, fail=None, inspected_items=0):
        self.items = items
        self.operation = operation
        self.test = test
        self.success = success
        self.fail = fail
        self.inspected_items = inspected_items

def read_file():
    f = open(DATA_FILE, "r")
    return f.read().splitlines()

def initial_state():
    monkeys = []
    monkey = None
    test = None 
    success = None
    fail = None
    for line in read_file():
        if 'Monkey' in line:
            monkey = Monkey()
        elif 'Starting items:' in line:
            items = []
            l  = line.replace('Starting items: ', '').replace(' ', '')
            for a in l.split(','):
                items.append(int(a))
            monkey.items = items
        elif 'Operation: new = old ' in line:
            operation = line.replace('Operation: new = old ', '').replace(' ', '')
            monkey.operation = operation
        elif 'Test: divisible by ' in line:
            test = int(line.replace('Test: divisible by ', ''))
            monkey.test = test
        elif 'If true: throw to monkey ' in line:
            success = int(line.replace('If true: throw to monkey ', ''))
            monkey.success = success
        elif 'If false: throw to monkey ' in line:
            fail = int(line.replace('If false: throw to monkey ', ''))
            monkey.fail = fail
            monkeys.append(monkey)

    return monkeys

def print_monkeys(monkeys):
    i = 0
    for monkey in monkeys:
        print(i, '->', monkey.items, monkey.inspected_items)
        i+=1

def get_worry_level(monkey, item, active_worry_level):
    worry_level = None
    if 'old' in monkey.operation:
        worry_level = item*item
    else:
        worry_level = eval(str(item)+monkey.operation)

    #lcm = 1
    #if active_worry_level:
    #    mcm = math.lcm(*monkey.items)
    #    if worry_level > mcm and worry_level % mcm == 0:
    #        lcm = mcm

    return math.floor(worry_level / 3) if active_worry_level else math.floor(worry_level)

def get_monkey_to_move(worry_level, monkey):
    to_monkey = None
    if (worry_level % monkey.test) == 0:
        to_monkey = monkey.success
    else:
        to_monkey = monkey.fail
    return to_monkey 

def calculate_rounds(monkeys, rounds, active_worry_level):
    for r in  range(1, rounds+1):
        #print(r)
        for monkey in monkeys:
            monkey.inspected_items += len(monkey.items)
            for item in monkey.items:
                worry_level = get_worry_level(monkey, item, active_worry_level)
                to_monkey = get_monkey_to_move(worry_level, monkey)
                monkeys[to_monkey].items.append(worry_level)
            monkey.items = []
    
    print_monkeys(monkeys)


def part_one():
    monkeys = initial_state()
    calculate_rounds(monkeys, 20, True)
    inspected_items = []
    for monkey in monkeys:
        inspected_items.append(monkey.inspected_items)
    inspected_items.sort()
    monkey_business = inspected_items[-1] * inspected_items[-2]
    print("PART ONE:", monkey_business)

def part_two():
    #disable Exceeds the limit (4300) for integer string conversion
    sys.set_int_max_str_digits(1_000_000) 
    monkeys = initial_state()
    calculate_rounds(monkeys, 1, False)
    inspected_items = []
    for monkey in monkeys:
        inspected_items.append(monkey.inspected_items)
    inspected_items.sort()
    print(inspected_items)
    print("lcm", math.lcm(inspected_items[-1], inspected_items[-2]))
    lcm = math.lcm(2, 3, 8, 8, 8, 9, 16, 19)
    #print(inspected_items[-1] * lcm * inspected_items[-2] * inspected_items[-1])
    inspected_items = [item * lcm for item in inspected_items]
    print(inspected_items)
    monkey_business = inspected_items[-1] * inspected_items[-2]
    print("PART TWO:", monkey_business)
    #25272176808
    #2275651584

if __name__ == "__main__":
    part_one()
    part_two()