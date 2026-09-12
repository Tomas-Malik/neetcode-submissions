
class Solution:

    def compare(self, left: list[int], right: list[int]) -> bool:
        #if left <= right: return True, else False
        l_dist_to_origin = math.sqrt(left[0]**2 + left[1]**2)
        r_dist_to_origin = math.sqrt(right[0]**2 + right[1]**2)
        if l_dist_to_origin <= r_dist_to_origin:
            return True
        else:
            return False


    def merge(self, left: list[list[int]], right: list[list[int]]) -> list[list[int]]:

        if not left:
            return right
        if not right:
            return left
        
        merged_list = []
        i,j = 0,0
        while i < len(left) or j < len(right):
            if (i == len(left)):
                merged_list.append(right[j])
                j += 1
                continue
            if (j == len(right)):
                merged_list.append(left[i])
                i += 1
                continue
            
            #both lists still exist
            left_val = left[i]
            right_val = right[j]

            if self.compare(left_val,right_val):
                merged_list.append(left_val)
                i += 1
            else:
                merged_list.append(right_val)
                j += 1
        return merged_list



    def merge_sort(self, arr: list[list[int]]) -> list[list[int]]:
        if len(arr) <= 1:
            return arr
        
        mid_point = len(arr) //2
        left_half = arr[:mid_point]
        right_half = arr[mid_point:]

        sorted_left_half = self.merge_sort(left_half)
        sorted_right_half = self.merge_sort(right_half)

        return self.merge(sorted_left_half, sorted_right_half)


    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points or k == 0:
            return []
        ans_list = []
        sorted_points = self.merge_sort(points)
        

        return sorted_points[:k]
        

        