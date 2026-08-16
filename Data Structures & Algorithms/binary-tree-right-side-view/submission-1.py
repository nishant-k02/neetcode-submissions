# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Solution 1: using reverse preorder traversal

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        resultArray = []
        def dfs(node, level):
            nonlocal resultArray
            if not node:
                return []
            if level == len(resultArray):
                resultArray.append(node.val)

            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        dfs(root, 0)
        return resultArray

        