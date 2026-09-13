class Solution:
    def matrixDFS(self,grid: list[list[int]], cr: int, cc: int) -> list[list[int]]:
        if cr < 0 or cc < 0 or cr == len(grid) or cc == len(grid[0]) or (grid[cr][cc] == "0"):
            return grid
        
        #mark land as water
        grid[cr][cc] = "0"

        grid = self.matrixDFS(grid, cr+1, cc)
        grid = self.matrixDFS(grid, cr-1, cc)
        grid = self.matrixDFS(grid, cr, cc+1)
        grid = self.matrixDFS(grid, cr, cc-1)

        return grid

    

    def numIslands(self, grid: List[List[str]]) -> int:
        ct = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    ct +=1
                    grid = self.matrixDFS(grid, i,j)
        return ct

        