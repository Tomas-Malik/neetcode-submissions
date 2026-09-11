# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False
        
        stack = [(root, targetSum-root.val)]
        
        while stack:
            cur, targetSum = stack.pop()
            
            if not cur.left and not cur.right and targetSum == 0:
                return True
            if cur.left:
                stack.append((cur.left,targetSum-cur.left.val))
            if cur.right:
                stack.append((cur.right,targetSum-cur.right.val))

        
        return False
            
            
               