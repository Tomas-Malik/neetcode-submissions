import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        new_stones = [-x for x in stones]
        heapq.heapify(new_stones)

        while len(new_stones) > 1:
            

            stone1 = heapq.heappop(new_stones)
            stone2 = heapq.heappop(new_stones)
            stone1 = -stone1
            stone2 = -stone2
            

            if stone1 == stone2:
                continue
            elif stone1 < stone2:
                stone2 = stone2 - stone1
                heapq.heappush(new_stones,-stone2)
            else:
                stone1 = stone1 - stone2
                heapq.heappush(new_stones,-stone1)
        if len(new_stones) == 1:

            final_stone = heapq.heappop(new_stones)
            final_stone = -final_stone        
            return final_stone
        else:
            return 0
        



        