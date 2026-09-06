class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        x = arr[l-1]
        mx = x 
        
        for i in range(1, l):
            
            if x > mx:
                mx = x
            x = arr[l-1-i]
            arr[l-1 - i] = mx
            

        arr[l-1] = -1
        return arr



