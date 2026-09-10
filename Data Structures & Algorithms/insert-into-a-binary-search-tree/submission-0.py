# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)
        if not root:
            return new_node
        cur = root
        lag = cur #lags behind current by one position
        while cur:
            lag = cur
            if val > cur.val:
                cur = cur.right
            else:
                cur = cur.left
        if val > lag.val:
            lag.right = new_node
        else:
            lag.left = new_node
        
        return root

        

        