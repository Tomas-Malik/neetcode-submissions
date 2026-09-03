class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # x = 1
        # zero_ct = 0
        # ix = -1
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         ix = i
        #         zero_ct +=1
        #         continue
        #     x = x * nums[i]
            
        # if zero_ct > 1:
        #     return [0]*len(nums)
        # elif zero_ct == 1:
        #     otp = [0]*len(nums)
        #     otp[ix] = x
        #     return otp

        x = 1
        otp = []
        left = []
        right = []
        left.append(1)
        for i in range(1, len(nums)):
            x = x * nums[i-1]
            left.append(x)
        y = 1
        right = [1]*len(nums)
        for i in range(len(nums)-1,0,-1):
            y = y * nums[i]
            right[i-1] = y
        for i in range(len(nums)):
            otp.append(left[i]*right[i])
        # print(left)
        # print(right)
        return otp


