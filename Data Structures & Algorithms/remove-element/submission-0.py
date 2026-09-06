class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ct = 0

        it = 0
        mx = len(nums)

        while it < mx:
            if nums[it] != val:
                ct +=1
                it +=1
                continue
            del nums[it]
            mx = mx - 1
        return ct
