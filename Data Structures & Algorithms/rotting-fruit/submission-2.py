class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #min 0
        # grid=[
        #     [2,1,1],
        #     [1,1,0],
        #     [0,1,1]
        #     ]
        

        q = deque()
        #visited = set()
        # I can spend 1 iter finding fresh fruits and then only check them and their neighbours for rotten, eliminating them as I iterate - faster than O(n^2*minute) <- its this at worse

        fresh_list = []
        
        minute = 0

        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_list.append((i,j))
        if not fresh_list:
            return 0
        flag = True
        new_list = []
        nbrs = [[-1,0], [1,0], [0,1],[0,-1]]
        
        while flag:
            
            
            new_list = list(fresh_list)
            fresh_list = []
            
            flag = False
            minute += 1
            rot_list = []
            for cr,cc in new_list:
                fruit_ok = True
                for dr,dc in nbrs:
                    cr_n = cr+dr
                    cc_n = cc + dc
                    if cr_n <0 or cc_n < 0 or cr_n == m or cc_n == n: #bounds
                        continue
                    if grid[cr_n][cc_n] == 2:
                        flag = True
                        rot_list.append((cr,cc))
                        fruit_ok = False
                if fruit_ok:
                    fresh_list.append((cr,cc))
            for cr,cc in rot_list:
                grid[cr][cc] = 2
            if fresh_list and new_list == fresh_list:
                return -1
            elif not fresh_list:
                return minute

            
                
                



        return minute


            

            




            

        


