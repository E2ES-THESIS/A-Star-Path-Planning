# A* Implementation
# Author : Jerrin Bright
# Copyrights : 2021

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]  # (r,c)
cost = 1

#print(len(grid), len(grid[0]))
print(goal)

delta = [[-1, 0 ], # up
         [ 0, -1], # left
         [ 1, 0 ], # down
         [ 0, 1 ]] # right

delta_name = ['^', '<', 'v', '>'] 

def search(grid,init,goal,cost,heuristic):

    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed[init[0]][init[1]] = 1

    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    action = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]

    x = init[0]
    y = init[1]
    g = 0
    f = g + heuristic[x][y]

    open = [[f, g, x, y]]

    found = False 
    resign = False 
    count = 0
    
    while not found and not resign:
        if len(open) == 0:
            resign = True
            return "Fail"
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            f = next[0]
            g = next[1]
            x = next[2]
            y = next[3]
            
            expand[x][y] = count
            count += 1
            
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            f = g2 + heuristic[x2][y2]
                            open.append([f, g2, x2, y2])
                            closed[x2][y2] = 1
                            
    return expand

result = search(grid,init,goal,cost,heuristic)

for el in result:
	print (el)

