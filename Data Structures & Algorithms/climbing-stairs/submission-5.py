class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        l = [0]*(n+1)
        
        l[0] = 1
        l[1] = 2
         
        
        for i in range(2,n+1):
            new_val = l[i-1] + l[i-2]
            l[i] = new_val
        return l[n-1]



            

        