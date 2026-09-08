class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        flag = False
        ix = 0
        

        while (l < r):
            
            half = (r-l) // 2 + l
            if nums[half] == target:
                ix = half
                flag = True
                break
            elif target < nums[half]:
                r = half
            else:
                l = half + 1
            

        if flag:
            return ix
        else:
            return -1
            




        