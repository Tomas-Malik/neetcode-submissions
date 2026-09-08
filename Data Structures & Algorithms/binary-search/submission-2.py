class Solution:
    def search(self, nums: List[int], target: int) -> int:
        flag = False
        if len(nums) == 0:
            return -1
        ix = 0
        while nums:
            half = len(nums) // 2
            if target == nums[half]:
                ix+= half
                nums = []
                flag = True
            elif target < nums[half]:
                nums = nums[:half]
            else:
                ix += half + 1
                nums = nums[half+1:]
        if flag:
            return ix
        else:
            return -1
        

            