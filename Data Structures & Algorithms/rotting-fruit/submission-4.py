class Solution:


    def orangesRotting(self, grid: List[List[int]]) -> int:
        #my bfs solution
        #track change
        # grid=[
        #     [1,1,0],
        #     [0,1,1],
        #     [0,1,2]]

        minute = 0
        q = deque()
        fresh_fruit_exist = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh_fruit_exist = True

        if not fresh_fruit_exist:
            return 0
        nbrs = [[-1,0], [1,0], [0,1], [0,-1]]
        minute = 0
        
        while len(q) > 0:
            
            for i in range(len(q)):
                cr,cc = q.popleft()
                for dr,dc in nbrs:
                    cr_n = cr + dr
                    cc_n = cc + dc
                    if cr_n < 0 or cc_n < 0 or cr_n == len(grid) or cc_n == len(grid[0]):
                        continue
                    if grid[cr_n][cc_n] == 1:
                        grid[cr_n][cc_n] =2
                        q.append((cr_n,cc_n))
                
            minute += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        return minute -1 
                







           



        