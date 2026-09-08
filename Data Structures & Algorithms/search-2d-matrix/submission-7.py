class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        flag = False
        for i in matrix:
            if i:
                flag = True
        if not flag:
            return False

        # I would need to remove all empty rows if any

        l = 0
        m_len = len(matrix)
        n_len = len(matrix[0])
        r = m_len*n_len
        

        while l < r:
            half = (r-l) // 2 + l
            m = half // n_len
            n = half % n_len
            if matrix[m][n] == target:
                return True
            elif target < matrix[m][n]:
                r = half
            else:
                l = half + 1
        return False

        