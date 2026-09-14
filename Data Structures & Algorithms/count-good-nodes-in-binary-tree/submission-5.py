# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maximumValue):
            if not node:
                return 0
            
            if node.val >= maximumValue:
                res = 1
            else:
                res = 0
            
            maximumValue = max(maximumValue, node.val)

            res += dfs(node.left, maximumValue)
            res += dfs(node.right, maximumValue)

            return res

        return dfs(root, root.val)
            
        