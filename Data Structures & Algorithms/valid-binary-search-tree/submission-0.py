# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, min_allowed, max_allowed):
            if not node:
                return True

            if node.val <= min_allowed or node.val >= max_allowed:
                return False
            left = validate(node.left, min_allowed, node.val)
            right = validate(node.right, node.val, max_allowed)

            return left and right
        return validate(root, float('-inf'), float('inf'))
        