class Solution:
    def climbStairs(self, n: int) -> int:
        k = 1
        l = 2
        if n <= 2:
            m = n
        for i in range(3,n+1):
            m = k+l
            k = l
            l = m
        return m
        