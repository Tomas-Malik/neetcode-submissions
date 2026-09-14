class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) ==2:
            return max(nums[1], nums[0])

        booty = [0]*len(nums)
        booty[0] = nums[0]
        booty[1] = max(nums[0], nums[1])

        for j in range(2, len(nums)):
            booty[j] = max(booty[j-2] + nums[j], booty[j-1])
        
        return booty[-1]


