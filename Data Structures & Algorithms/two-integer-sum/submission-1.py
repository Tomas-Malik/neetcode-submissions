class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_l = {}
        for i in range(len(nums)):
            if nums[i] in new_l:
                return [new_l[nums[i]],i]
            else: 
                new_l[target - nums[i]] = i
