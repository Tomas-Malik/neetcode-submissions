
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        half = len(nums) // 2
        if not nums:
            return -1
        if nums[half] == target:
            return half
        elif target < nums[half]:
            ix = self.search(nums[:half], target)
        else:
            acc = half + 1
            ix = self.search(nums[half+1:], target)
            if ix != -1:
                ix = acc + ix
        return ix