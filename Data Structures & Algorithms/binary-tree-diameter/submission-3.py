# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = 0

        def diameterBT(node):
            nonlocal diameter

            if not node:
                return 0
            
            leftHeight = diameterBT(node.left)
            rightHeight = diameterBT(node.right)

            diameter = max(diameter, (leftHeight + rightHeight))

            return 1 + max(leftHeight, rightHeight)
        
        diameterBT(root)
        return diameter
        