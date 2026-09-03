class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        otp = []
        x = 1
        zero_ct = 0
        ix = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                ix = i
                zero_ct +=1
                continue
            x = x * nums[i]
            

        if zero_ct > 1:
            return [0]*len(nums)
        elif zero_ct == 1:
            otp = [0]*len(nums)
            otp[ix] = x
            return otp

        

        for i in range(len(nums)):
            otp.append(int(x/nums[i]))
        return otp



        