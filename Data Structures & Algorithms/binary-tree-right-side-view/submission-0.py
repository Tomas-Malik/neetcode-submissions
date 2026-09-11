# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        otp_list = []

        if not root:
            return []
        
        
        q = deque()
        q.append(root)
        otp_list.append(root.val)

        while len(q) > 0:
            children = []
            for i in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    children.append(cur.left)
                    q.append(cur.left)
                if cur.right:
                    children.append(cur.right)
                    q.append(cur.right)
            if children:
                cur = children[-1]
                otp_list.append(cur.val)
            
        return otp_list



            
            
            


        