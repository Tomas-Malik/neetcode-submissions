class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pt1, pt2 = 0, len(numbers)-1
        for i in range(len(numbers)):
            s = numbers[pt1] + numbers[pt2]
            if s == target:
                return [pt1+1, pt2+1]
            elif s < target:
                pt1 += 1
            else:
                pt2 -= 1
