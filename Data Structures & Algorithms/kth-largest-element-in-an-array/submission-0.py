import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #I have two options: sort -> i am a friend of merge_sort + merge, heap
        heapq.heapify(nums)
        
        k = len(nums) - k # [1,2,3,4,5], len() = 5, k = 2, target = 4, new k = 3
        for i in range(k):
            heapq.heappop(nums)
        return heapq.heappop(nums)
