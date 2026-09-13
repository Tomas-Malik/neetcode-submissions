class Solution:

    def matrixDFS(self, grid: List[List[int]], cr: int,cc: int) -> int:
        if cr < 0 or cc < 0 or cr == len(grid) or cc == len(grid[0]) or grid[cr][cc] == 0:
            return 0
        
        grid[cr][cc] = 0
        
        
        island_size = 1
        island_size += self.matrixDFS(grid, cr+1, cc)
        island_size += self.matrixDFS(grid, cr-1, cc)
        island_size += self.matrixDFS(grid, cr, cc+1)
        island_size += self.matrixDFS(grid, cr, cc-1)

        return island_size

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_size = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    
                    island_size = self.matrixDFS(grid, i, j)
                    if island_size > max_size:
                        max_size = island_size
        
        return max_size
        