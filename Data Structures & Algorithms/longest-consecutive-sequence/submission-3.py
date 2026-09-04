class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        if len(nums) == 0:
            return 0
        longest = 1
        
        for i in nums:
            current =1 
            if i-1 in st:
                continue
            
            while (i + current) in st:
                current +=1
            if current > longest:
                longest = current
        return longest
                
                
            