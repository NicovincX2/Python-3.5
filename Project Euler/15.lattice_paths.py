# -*- coding: utf-8 -*-

"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""

import os

def lattice_paths(squares):
    gridsize = squares+1
    grid = [[0 for i in range(gridsize)] for j in range(gridsize)]
    row, col = 0, 0
    
    while col < gridsize:     
        while row < gridsize: 
        
            if row == 0 and col == 0:
                grid[row][col] = 1
            
            else:
                if row == 0 and col != 0:
                    grid[row][col] += grid[row][col-1]
                elif row != 0 and col == 0:
                    grid[row][col] += grid[row-1][col]  
                else:
                    grid[row][col] += grid[row][col-1] + grid[row-1][col] 
            
            row += 1 
        row = 0
        col += 1       
    return grid[gridsize-1][gridsize-1]
   
def main():
    import time
    start = time.time() 
    
    assert(lattice_paths(2) == 6)
    print(lattice_paths(20))
    
    elapsed = (time.time() - start)
    print('Tests Passed!\n It took %s seconds to run them.' % (elapsed))   
                   
if __name__ == '__main__':
    main()

os.system("pause")