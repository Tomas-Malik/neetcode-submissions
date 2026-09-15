class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == "" or text2 == "":
            return 0
        
        m = len(text1)
        n = len(text2)

        matrix = []
        for i in range(m+1):
            row = [0]*(n+1)
            matrix.append(row)
        
        for i in range(m-1, -1,-1):
            for j in range(n-1,-1,-1):
                if text1[i] == text2[j]:
                    matrix[i][j] = 1 + matrix[i+1][j+1]
                else:
                    matrix[i][j] = max(matrix[i+1][j], matrix[i][j+1])
        
        return matrix[0][0]

        

