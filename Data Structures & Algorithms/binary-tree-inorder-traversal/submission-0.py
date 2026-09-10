# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans_list = []

        def helper_inorder(root):
            if not root:
                return
            
            helper_inorder(root.left)
            ans_list.append(root.val)
            helper_inorder(root.right)

        helper_inorder(root)
        
        return ans_list