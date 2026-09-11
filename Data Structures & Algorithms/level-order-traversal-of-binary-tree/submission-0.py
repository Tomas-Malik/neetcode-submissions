# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        otp_list = []

        if not root:
            return otp_list
        
        q = deque()
        q.append(root)

        level_list = [] 
        while len(q) > 0:
            children = []
            for i in range(len(q)):
                cur = q.popleft()
                children.append(cur)
                level_list.append(cur.val)
            otp_list.append(level_list)
            for cur in children:
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            
            level_list = []

        
        return otp_list


        