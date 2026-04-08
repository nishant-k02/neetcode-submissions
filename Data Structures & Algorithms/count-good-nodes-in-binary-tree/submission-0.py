# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maximum):
            if not node:
                return 0
            is_good = 1 if node.val >= maximum else 0

            maximum = max(maximum, node.val)

            left_count = dfs(node.left, maximum)
            right_count = dfs(node.right, maximum)
            return is_good + left_count + right_count
        
        return dfs(root, root.val)


        