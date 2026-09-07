
class Solution:
    def compare(self, point1: List[int], point2: List[int]) -> int:
        val1 = math.sqrt((point1[0])**2 + (point1[1])**2)
        val2 = math.sqrt((point2[0])**2 + (point2[1])**2)
        if val1 < val2:
            return 0
        return 1


    def weirdSort(self, points: List[List[int]], s:int, e:int) -> List[List[int]]:
        if e-s+1 <= 1:
            return points
        
        pivot = points[e]
        left = s

        for i in range(s,e):
            if self.compare(points[i], pivot) == 0:
                tmp = points[left]
                points[left] = points[i]
                points[i] = tmp
                left +=1
        
        points[e] = points[left]
        points[left] = pivot
        
        self.weirdSort(points, s, left-1)
        self.weirdSort(points, left+1, e)
        return points


    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        s = 0
        e = len(points)-1
        points = self.weirdSort(points, s, e)
        print(points)
        return points[:k]







        