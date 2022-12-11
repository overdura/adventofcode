# -*- coding: utf-8 -*-
DATA_FILE='data.in'


def read_file():
    f = open(DATA_FILE, "r")
    return f.readlines()

def clean_line(line):
    return line.replace('\n', '')

def get_grid():
    grid = []
    lines = read_file()
    column = 0
    for line in lines:
        row = clean_line(line)
        grid.append([int(r) for r in row])
        column+=1
    return grid

def is_not_visible(current_tree, compare_tree):
    return compare_tree >= current_tree

def is_current_blocked(current_tree, compare_tree):
    return current_tree <= compare_tree

def get_subgrid(x_ini, y_ini, x_end, y_end, grid, x_counter=True, y_counter=True):
    result = []
    while x_ini <= x_end and y_ini <= y_end:
        result.append(grid[x_ini][y_ini])
        if not x_counter:
            x_ini += 1
        if not y_counter:
            y_ini += 1
    return result

def is_current_visible(current_tree, trees):
    visible = True
    for tree in trees:
        if is_not_visible(current_tree, tree):
            return False
    return visible

def tree_best_alternative_is_visible(current_row, current_column, grid):
    visible = False
    current_tree = grid[current_row][current_column]
    top_subgrid = get_subgrid(x_ini=0, y_ini=current_column, x_end=current_row-1, y_end=current_column, grid=grid, x_counter=False)
    top_subgrid.reverse()
    top_visible = is_current_visible(current_tree, top_subgrid)
    bottom_subgrid = get_subgrid(x_ini=current_row+1, y_ini=current_column, x_end=len(grid)-1, y_end=current_column, grid=grid, x_counter=False)
    bottom_visible = is_current_visible(current_tree, bottom_subgrid)
    right_subgrid = get_subgrid(x_ini=current_row, y_ini=current_column+1, x_end=current_row, y_end=len(grid[0])-1, grid=grid, y_counter=False)
    right_visible = is_current_visible(current_tree, right_subgrid)
    left_subgrid = get_subgrid(x_ini=current_row, y_ini=0, x_end=current_row, y_end=current_column-1, grid=grid, y_counter=False)
    left_subgrid.reverse()
    left_visible = is_current_visible(current_tree, left_subgrid)

    if top_visible or right_visible or bottom_visible or left_visible:
        return True
    return visible

def get_visible_trees(grid):
    visible_trees = 0
    total_rows_inside = len(grid)-1
    total_columns_inside = len(grid[0])-1
    for row_index in range(1, total_rows_inside):
        for column_index in range(1, total_columns_inside):
            #if (tree_is_visible(row_index, column_index, grid)): ORIGINAL
            if (tree_best_alternative_is_visible(row_index, column_index, grid)):
                visible_trees += 1
    visible_edge = ((len(grid)-2) * 4) + 4
    return visible_edge + visible_trees

def tree_score(current_tree, trees):
    score = 0
    for tree in trees:
        score+=1
        if is_current_blocked(current_tree, tree):
            break
    return score

def get_best_alternative_tree_scenic_score(current_row, current_column, grid):
    score = 0
    current_tree = grid[current_row][current_column]
    top_subgrid = get_subgrid(x_ini=0, y_ini=current_column, x_end=current_row-1, y_end=current_column, grid=grid, x_counter=False)
    top_subgrid.reverse()
    top = tree_score(current_tree, top_subgrid)
    bottom_subgrid = get_subgrid(x_ini=current_row+1, y_ini=current_column, x_end=len(grid)-1, y_end=current_column, grid=grid, x_counter=False)
    bottom = tree_score(current_tree, bottom_subgrid)
    right_subgrid = get_subgrid(x_ini=current_row, y_ini=current_column+1, x_end=current_row, y_end=len(grid[0])-1, grid=grid, y_counter=False)
    right = tree_score(current_tree, right_subgrid)
    left_subgrid = get_subgrid(x_ini=current_row, y_ini=0, x_end=current_row, y_end=current_column-1, grid=grid, y_counter=False)
    left_subgrid.reverse()
    left =  tree_score(current_tree, left_subgrid)

    score = top * left * bottom *  right
    return score
    
def get_scenic_scores(grid):
    scenic_scores = []
    total_rows_inside = len(grid)-1
    total_columns_inside = len(grid[0])-1
    for row_index in range(1, total_rows_inside):
        for column_index in range(1, total_columns_inside):
            #ORIGINAL
            #scenic_scores.append(get_tree_scenic_score(row_index, column_index, grid))
            scenic_scores.append(get_best_alternative_tree_scenic_score(row_index, column_index, grid))
            
    return scenic_scores

def part_one():
    grid = get_grid()
    visible_trees = get_visible_trees(grid)
    print("PART ONE visible trees: ", visible_trees)

def part_two():
    grid = get_grid()
    scenic_scores = get_scenic_scores(grid)
    scenic_scores.sort()
    print("PART TWO highest scenic score: ", scenic_scores[len(scenic_scores)-1]) 

if __name__ == "__main__":
    part_one()
    part_two()

'''
def tree_is_visible(current_row, current_column, grid):
    visible = False
    current_tree = grid[current_row][current_column]
    top_visible = is_top_visible(current_tree, current_row, current_column, grid)
    right_visible = is_right_visible(current_tree, current_row, current_column, grid)
    bottom_visible = is_bottom_visible(current_tree, current_row, current_column, grid)
    left_visible = is_left_visible(current_tree, current_row, current_column, grid)

    if top_visible or right_visible or bottom_visible or left_visible:
        return True
    
    return visible
    
def is_visible(current_tree, compare_tree):
    return current_tree > compare_tree
    
def is_top_visible(current_tree, current_tree_row, current_tree_column, grid):
    visible = True
    row_index = current_tree_row-1
    while (row_index >= 0):
        compare_tree = grid[row_index][current_tree_column]
        if not is_visible(current_tree, compare_tree):
            return False
        row_index -= 1
    return visible

def is_right_visible(current_tree, current_tree_row, current_tree_column, grid):
    visible = True
    column_index = current_tree_column+1
    while (column_index <= len(grid[0])-1):
        compare_tree = grid[current_tree_row][column_index]
        if not is_visible(current_tree, compare_tree):
            return False
        column_index += 1
    return visible

def is_bottom_visible(current_tree, current_tree_row, current_tree_column, grid):
    visible = True
    row_index = current_tree_row+1
    while (row_index <= len(grid)-1):
        compare_tree = grid[row_index][current_tree_column]
        if not is_visible(current_tree, compare_tree):
            return False
        row_index += 1
    return visible

def is_left_visible(current_tree, current_tree_row, current_tree_column, grid):
    visible = True
    column_index = current_tree_column-1
    while (column_index >= 0):
        compare_tree = grid[current_tree_row][column_index]
        if not is_visible(current_tree, compare_tree):
            return False

        column_index -= 1
    return visible

def top_score(current_tree, current_tree_row, current_tree_column, grid):
    score = 0
    row_index = current_tree_row-1
    while (row_index >= 0):
        compare_tree = grid[row_index][current_tree_column]
        score+=1
        if is_current_blocked(current_tree, compare_tree):
            break
        row_index -= 1
    return score

def right_score(current_tree, current_tree_row, current_tree_column, grid):
    score = 0
    column_index = current_tree_column+1
    while (column_index <= len(grid[0])-1):
        compare_tree = grid[current_tree_row][column_index]
        score+=1
        if is_current_blocked(current_tree, compare_tree):
            break
        column_index += 1
    return score

def bottom_score(current_tree, current_tree_row, current_tree_column, grid):
    score = 0
    row_index = current_tree_row+1
    while (row_index <= len(grid)-1):
        compare_tree = grid[row_index][current_tree_column]
        score+=1
        if is_current_blocked(current_tree, compare_tree):
            break
        row_index += 1
    return score

def left_score(current_tree, current_tree_row, current_tree_column, grid):
    score = 0
    column_index = current_tree_column-1
    while (column_index >= 0):
        compare_tree = grid[current_tree_row][column_index]
        score+=1
        if is_current_blocked(current_tree, compare_tree):
            break
        column_index -= 1
    return score

def get_tree_scenic_score(current_row, current_column, grid):
    score = 0
    current_tree = grid[current_row][current_column]
    top = top_score(current_tree, current_row, current_column, grid)
    right = right_score(current_tree, current_row, current_column, grid)
    bottom = bottom_score(current_tree, current_row, current_column, grid)
    left = left_score(current_tree, current_row, current_column, grid)
    score = top * right* bottom * left
    return score
'''