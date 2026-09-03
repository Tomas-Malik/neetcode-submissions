class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            #pretty thing #1
            count[i] = count.get(i, 0) + 1 #this is the same as my if statement that either increments value of key or inserts a key,val
        
        n = len(nums)

        #here is the really smart solution
        buckets = [[] for _ in range(n + 1)]  # index = frequency

        for num, freq in count.items():
            buckets[freq].append(num)
        
        otp = []
        for freq in range(n, 0, -1): #reverse order loop
            for num in buckets[freq]:
                otp.append(num)
                if len(otp) == k:
                    return otp
        
        return otp