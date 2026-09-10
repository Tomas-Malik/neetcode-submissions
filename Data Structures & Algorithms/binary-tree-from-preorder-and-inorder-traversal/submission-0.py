# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        mapping = {}
        for ix, val in enumerate(inorder):
            mapping[val] = ix
        preorder_index = 0
        
        def build(low, high):
            if low > high:
                return None
            nonlocal preorder_index

            root_val = preorder[preorder_index]
            preorder_index += 1
            root = TreeNode(root_val)
            mid = mapping[root_val]
            root.left = build(low, mid - 1)
            root.right = build(mid+1, high)
            return root

        root = build(0,len(inorder)-1)
        return root

