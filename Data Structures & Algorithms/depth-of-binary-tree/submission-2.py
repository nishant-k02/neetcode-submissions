# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        maxDepth = 0
        def height(node):
            nonlocal maxDepth

            if not node:
                return 0
            
            leftHeight = height(node.left)
            rightHeight = height(node.right)

            maxDepth = 1 + max(leftHeight, rightHeight)

            return maxDepth
        
        return height(root)
            
            

        