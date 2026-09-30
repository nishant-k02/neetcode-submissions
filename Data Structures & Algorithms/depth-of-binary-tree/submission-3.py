# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        maxDepth = 0

        def depth(node):
            nonlocal maxDepth

            # base case
            if not node:
                return 0
            
            # finding left and right height
            leftHeight = depth(node.left)
            rightHeight = depth(node.right)

            # returning current level height and selecting maximum
            maxDepth = 1 + max(leftHeight, rightHeight)

            return maxDepth
        
        return depth(root)
        
            
            

        