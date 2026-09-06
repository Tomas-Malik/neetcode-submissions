class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = [0] * (2*l)

        for i in range(l):
            ans[i] = nums[i]
            ans[i+l] = nums[i]
        return ans