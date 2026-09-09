class Solution:

    def check_eating_rate(self,piles: list[int], candidate: int, hour_limit: int) -> bool:
        if candidate == 0:
            return False
        for pile in piles:
            floor_div = pile // candidate
            remainder = pile % candidate
            if remainder == 0:
                pile_consumption_hours = floor_div
            else:
                pile_consumption_hours = floor_div + 1 
            hour_limit = hour_limit - pile_consumption_hours
            if hour_limit < 0: #ran out of hours
                return False
        return True




    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        length_piles = len(piles)
        max_pile = max(piles) # O(n), n = length_piles
        
        #binary search setup - to search for min. viable banana eating rate
        l = 0
        r = max_pile
        last_valid = max_pile
        while l <= r:
            mid = (r-l) // 2 + l
            if self.check_eating_rate(piles, mid, h):
                last_valid = mid
                r = mid - 1
            else:
                l = mid + 1
        return last_valid










