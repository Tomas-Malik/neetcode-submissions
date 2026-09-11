class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #
        
        ans = []
        cur_subset = []
        def dfs(i):
            if i >= len(nums):
                ans.append(list(cur_subset))
                print("ans update")
                return
            #include number
            cur_subset.append(nums[i])
            
            print("left branch")
            print(cur_subset)
            dfs(i+1)
            #dont include number
            cur_subset.pop()
            
            print("right branch")
            print(cur_subset)
            dfs(i+1)
        dfs(0)
        return ans

            
            


            

        



