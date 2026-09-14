class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        
        matrix = []
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1:
            return 0
        for i in range(m):
            row = [0] * n
            matrix.append(row)
        
        #-1 to mark a block
        for i in range(m):
            for j in range(n):
                row_ix = m-1-i
                col_ix = n-1-j
                #check bounds
                if (row_ix+1 == m or obstacleGrid[row_ix +1][col_ix] == 1) and (col_ix+1 == n or obstacleGrid[row_ix][col_ix+1] == 1) and (row_ix != m-1 or col_ix != n-1):
                    obstacleGrid[row_ix][col_ix] = 1
                    
        
        matrix[m-1][n-1] = 1
        for i in range(m):
            for j in range(n):
                row_ix = m-1-i
                col_ix = n-1-j
                if obstacleGrid[row_ix][col_ix] != 1:
                    if row_ix == m-1 and col_ix == n-1:
                        continue
                    val1 = 0
                    val2 = 0
                    if (row_ix+1 < m) and obstacleGrid[row_ix+1][col_ix] != 1:
                        val1= matrix[row_ix+1][col_ix]
                    if (col_ix+1 < n) and obstacleGrid[row_ix][col_ix+1] != 1:
                        val2 = matrix[row_ix][col_ix+1]
                    matrix[row_ix][col_ix] = val1 + val2
       
        return matrix[0][0]



                

        

        
                




                