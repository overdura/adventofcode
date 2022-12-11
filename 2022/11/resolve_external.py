from math import lcm, prod
from collections import defaultdict


class Monkey:
    monkeyNo=0
    items=[]
    operation=""
    testDiv=0
    testTrue=0
    testFalse = 0
    
    
   
monkeys = []
with open("data.in") as f:
    lines = f.readlines()
i=0
opers=[]
# mn=Monkey()
for line in lines:
    line = line.replace("\n", "")
    if "Monkey" in line:
        # get no form "Monkey 7:"
        
        i = int(line.split("Monkey ")[1].split(":")[0])
        mn = Monkey()
        mn.monkeyNo=i
    elif "Starting items" in line:
        
        items=line.split(":")[1]
        if "," in items:
            mn.items = list(map(int, items.strip().split(",")))
        else:
            mn.items = list(map(int, items.strip().split(" ")))
    elif "Operation" in line:
        op=line.split("= ")[1]
        
            # print(mn.operation(items[0]), items[0])
        
            
            # print(mn.operation(items[0]),items[0],op[1])
        mn.operation=op
    elif "Test" in line:
        test = int(line.split("Test: divisible by ")[1])
        # tests.append(test)
        mn.testDiv=int(test)
    elif "If true" in line:
        mn.testTrue= int(line.split("monkey ")[1])
    elif "If false" in line:
        mn.testFalse= int(line.split("monkey ")[1])
        monkeys.append(mn)     
# print(opers)
worries = []
for m in monkeys:
    worries.append(m.testDiv)
# print(w)

def solve(num_rounds, part1,monkeys):

    i = 0
    inspected = defaultdict(int)
    for _ in range(num_rounds * len(monkeys)):
        items = monkeys[i].items
        
        for item in items:
            # monkeys[i].inspected += 1
            inspected[i] += 1
            
            # new = monkeys[i].operation(item)
            # print(i,new,item)
            # new = opers[i](item)
            op = monkeys[i].operation.split(" ")
            # print(op)
            if op[-1] == "old":
                # current value
                if op[1] == "*":
                    new= item * item
            else:    # v = int(op[-1])
                if op[1] == "+":
                    new = item + int(op[-1])
                if op[1] == "*":
                    new= item * int(op[-1])
            # break
            # new = ops[i](item)
            new %= lcm(*worries)
            if part1:
                new //= 3
            
            if new % monkeys[i].testDiv == 0:
                monkeys[monkeys[i].testTrue].items.append(new)
            else:
                monkeys[monkeys[i].testFalse].items.append(new)
                    
                    
        monkeys[i].items = []
        i = (i + 1) % len(monkeys)
    print(inspected)
    return prod(sorted(inspected.values())[-2:])
# print("Part 1:",solve(20, True,monkeys))
print("Part 2:", solve(10_000, False, monkeys))