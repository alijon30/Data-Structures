You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def DFS(matrix, x, y):
            
            if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
                return 0
            
            if matrix[x][y] == 0:
                return 0
            
            matrix[x][y] = 0
            
            area = 1
            
            
            area += DFS(matrix, x+1, y)
            area += DFS(matrix, x -1, y)
            area += DFS(matrix, x, y+ 1)
            area += DFS(matrix, x, y-1)
            
            return area
        
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, DFS(grid, i, j))
        
        return max_area
                    
