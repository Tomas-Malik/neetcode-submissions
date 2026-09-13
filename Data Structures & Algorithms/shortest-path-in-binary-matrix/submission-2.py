from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # grid=[
        #     [0,1,0,1,0],
        #     [1,0,0,0,1],
        #     [0,0,1,1,1],
        #     [0,0,0,0,0],
        #     [1,0,1,0,0]]
        top_left = grid[0][0]

        if top_left != 0:
            return -1

        q = deque()
        visited = set()
        q.append((0,0))
        length = 1
        while len(q) > 0:
            for i in range(len(q)):
                cr, cc = q.popleft()
                visited.add((cr,cc))
                if cr == (len(grid) - 1) and cc == (len(grid[0]) - 1):
                    return length

                nbrs = [
                    [-1,-1], [1,1], [-1,0], [-1,1], [0, -1], [0,1], [1,0],[1,-1]
                    ]
                for dr, dc in nbrs:
                    cr_n = cr + dr
                    cc_n = cc + dc
                    
                    if cr_n < 0 or cc_n < 0 or cr_n == len(grid) or cc_n == len(grid[0]) or grid[cr_n][cc_n] == 1 or (cr_n,cc_n) in visited:
                        continue
                    q.append((cr_n, cc_n))
            length += 1
            
            

        return -1
            













        