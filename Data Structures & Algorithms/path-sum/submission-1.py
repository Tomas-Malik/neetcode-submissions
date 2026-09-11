# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def helper(self, root, target):
        if not root:
            return False #might have to change this
        target = target - root.val
        
        

        if (not root.left and not root.right):
            if (target == 0):
                
                return True
            else:
                return False
        a = False
        if root.left:
            a = self.helper(root.left, target)
        if not a:
            if root.right:
                a = self.helper(root.right, target)
            
            target = target + root.val
        return a

        
        
        

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        a = self.helper(root, targetSum)

        return a
        
