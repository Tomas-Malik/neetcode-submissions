class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colour_counts = [0,0,0]

        for i in nums:
            colour_counts[i] +=1
        
        i = 0
        for ix, k in enumerate(colour_counts):
            for j in range(k):
                nums[i] = ix
                i +=1
        return

        