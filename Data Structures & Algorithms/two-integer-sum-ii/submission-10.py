class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ln = len(numbers)
        for i in range(ln):
            x = numbers[i]

            rest = target - x
            if rest < x:
                continue
            if rest > numbers[ln-1]:
                continue
            
            l = i+1
            h = ln-1
            print(l, h)
            while l <= h:
                mid = (l+h)//2

                if rest == numbers[mid]:
                    return [i+1, mid+1]
                elif rest < numbers[mid]:
                    h = mid-1
                else:
                    l = mid+1

