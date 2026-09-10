# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # def findMinNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     cur = root
    #     while cur and cur.left:
    #         cur = cur.left
    #     return cur


    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        #special case: empty tree given - empty tree returned
        if not root:
            return None

        cur = root
        parent = None

        #search for the Node we want deleted until you find it or traverse the whole tree
        while cur and key != cur.val:
            parent = cur

            if key < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        
        # if cur == None, then have traversed the tree without finding the  node
        if not cur:
            return root #nothing to delete

        #Case 1: cur has at most one child
        if not cur.left or not cur.right:
            child = cur.left if cur.left else cur.right 
            if parent:
                if parent.left == cur:
                    parent.left = child
                else:
                    parent.right = child
                return root
            else:
                return child

            
        #Case 2: cur (target Node to be deleted) has two children
        deleteNode = cur
        new_parent = None

        #find the minimum node in the right subtree:
        cur = cur.right
        while cur.left:
            new_parent = cur
            cur = cur.left
        
        if new_parent:
            new_parent.left = cur.right
            cur.right = deleteNode.right
        
        cur.left = deleteNode.left
        if parent:
            if parent.left == deleteNode:
                parent.left = cur
            else:
                parent.right = cur
            return root
        
        
        return cur

        








        
        

            

        

            
        














