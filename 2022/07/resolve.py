# -*- coding: utf-8 -*-

#from collections import OrderedDict

DATA_FILE='data.in'
LIMIT_SIZE_PART_ONE = 100000
TOTAL_DISK = 70000000
LIMIT_SIZE_PART_TWO = 30000000
#DIR_SIZES = OrderedDict()
DIR_SIZES = {}

class Node:
    def __init__(self, name=None, data=None, prev=None, size=None):
        self.name = name
        self.prev = prev
        self.data = data
        self.size = size

def read_file():
    f = open(DATA_FILE, "r")
    return f.readlines()

def clean_line(line):
    return line.replace('\n', '')

def is_command(line):
    return True if line[0] == '$' else False

def get_node_by_name(child_nodes_current, name):
    for n in child_nodes_current:
        if n.name == name:
            return n

def get_parent_node(node):
    if node.prev == None:
        return node
    else:
        return get_parent_node(node.prev)

def create_filesystem():
    lines = read_file()
    node = Node(name='/')
    for line in lines:
        row = clean_line(line).split(' ')
        if is_command(row) and 'cd' in row:
            node_name = row[2]
            if node_name == '..': 
                node = node.prev
            elif node_name != '/': # node_name == / omitted
                node = get_node_by_name(node.data, node_name)
        elif is_command(row) and 'ls' in row:
            node.data = []
        else:
            size=None if 'dir' in row else int(row[0])
            node.data.append(Node(name=row[1], prev=node, size=size))
    return get_parent_node(node)

def print_tree(node, i=0):
    print(' '*i + node.name, node.size if node.size != None else '')
    if node.data == None:
        return
    for n in node.data:
        print_tree(n, i+1)

def calculate_dir_sizes(node, name=''):
    key = name+'|'+node.name if name != '' else node.name
    size = 0
    for n in node.data:
        if n.data != None:
            inside = calculate_dir_sizes(n, key)
            size += inside
        else:
            size += n.size
    DIR_SIZES[key] = size
    return size 

def get_size_to_delete(ordered_sizes, unused_disk):
    result = 0
    i = 0
    for o in ordered_sizes:
        result = unused_disk + o
        if (result > LIMIT_SIZE_PART_TWO):
         return ordered_sizes[i]
        i+=1
        

def part_one():
    total_size = 0
    filesystem = create_filesystem()
    calculate_dir_sizes(filesystem)
    for k in DIR_SIZES.keys():
        if DIR_SIZES[k] < LIMIT_SIZE_PART_ONE:
            total_size += DIR_SIZES[k]
    print("PART ONE total_size: ", total_size)

def part_two():
    total_size = 0
    filesystem = create_filesystem()
    calculate_dir_sizes(filesystem)
    used_disk = DIR_SIZES['/']
    unused_disk = TOTAL_DISK - used_disk 
    ordered_sizes = [DIR_SIZES[k]for k in DIR_SIZES.keys()]
    ordered_sizes.sort()
    min_size_delete = get_size_to_delete(ordered_sizes, unused_disk)
    print("PART TWO total_size: ", min_size_delete) 

if __name__ == "__main__":
    part_one()
    part_two()

