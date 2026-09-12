# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
       
        def height(node):

            if not node:
                return 0

            leftHeight = height(node.left)
            rightHeight = height(node.right)

            if leftHeight == -1 or rightHeight == -1:
                return -1
            
            if abs(leftHeight - rightHeight) > 1:
                return -1
            
            return 1 + max(leftHeight, rightHeight)
        
        return height(root) != -1
        
        