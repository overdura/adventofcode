# -*- coding: utf-8 -*-
DATA_FILE='data.in'

def external():
    with open(DATA_FILE) as file:
        dir = {
            'R': (1, 0),
            'L': (-1, 0),
            'U': (0, 1),
            'D': (0, -1),
        }

        moves = []
        for line in file:
            d, p = line.rstrip().split()
            moves.append((d, int(p)))

        def follow(head, tail):
            x, y = head[0] - tail[0], head[1] - tail[1] # diff 
            abs_x = abs(x)
            abs_y = abs(y)
            if abs_x > 1 or abs_y > 1:
                return (
                    tail[0] + (0 if x == 0 else x // abs_x),
                    tail[1] + (0 if y == 0 else y // abs_y)
                )
            return tail

        def solve(knots): 
            ropes = [(0, 0) for _ in range(knots)]
            tail_visited = {ropes[-1]} 
            for move in moves:
                vec = dir[move[0]]
                for _ in range(move[1]): # iterate in direction
                    H = ropes[0] # head
                    ropes[0] = H[0] + vec[0], H[1] + vec[1] # update head
                    for x in range(1, knots): # update all tails
                        ropes[x] = follow(ropes[x-1], ropes[x])
                    tail_visited.add(ropes[-1])
            return len(tail_visited)

        print(solve(knots=2)) # part 1
        print(solve(knots=10)) # part 2
        

if __name__ == "__main__":
    external()
