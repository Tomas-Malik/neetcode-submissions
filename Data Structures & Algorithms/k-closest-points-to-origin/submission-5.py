class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dct = {}
        dist_list = []
        for i in points:
            dist = math.sqrt(i[0]**2 + i[1]**2)
            if dist in dct:
                dct[dist].append([i[0],i[1]])
            else:
                dct[dist] = [[i[0],i[1]]]
                dist_list.append(dist)
        
        heapq.heapify(dist_list)
        ans_list = []
        i = 0
        while i < k:
            
            

            smallest_dist = heapq.heappop(dist_list)
            
            smallest_dist_opts = dct[smallest_dist]
            for j in smallest_dist_opts:
                if i < k:

                    ans_list.append(j)
                    i+=1
        return ans_list



        