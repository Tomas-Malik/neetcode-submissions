class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix=[]
        for i in range(m):
            row = [0]*n 
            row[-1] = 1
            if i == m-1:
                row = [1]*n
            matrix.append(row)
        
        for i in range(m-1):
            for j in range(n-1):
                row_ix = m-2 - i
                col_ix = n-2 - j
                matrix[row_ix][col_ix] = matrix[row_ix+1][col_ix] + matrix[row_ix][col_ix+1]
        
        return matrix[0][0]
        

            
        

