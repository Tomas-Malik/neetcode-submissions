class Solution:
    def climbStairs(self, n: int) -> int:
        l = [0] * n
        if n <=2:
            return n
        l[0] = 1
        l[1] = 2
        for i in range(2,n):
            l[i] = l[i-1] + l[i-2]
        
        return l[-1]
