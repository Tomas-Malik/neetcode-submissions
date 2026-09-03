class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dct = {}
        ix = 0
        for i in nums:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
        otp = []
        for i in range(k):
            max = 0
            targ_int = -1

            for key, val in dct.items():
                if val > max:
                    targ_int = key
                    max = val
            otp.append(targ_int)
            dct[targ_int] = -1
        return otp



        
        
            



