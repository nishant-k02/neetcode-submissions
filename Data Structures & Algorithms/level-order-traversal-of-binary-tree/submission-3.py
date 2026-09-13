# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # base case
        if not root:
            return []

        resultArray = []        # stores final array with level order array
        levelArray = []         # stores each level array on iteration

        queue = deque()
        queue.append(root)

        while queue:

            size = len(queue)

            for i in range(size):
                currentNode = queue.popleft()
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
        
                levelArray.append(currentNode.val)

            # level iteration ended, check if any node present or not, if present, add to result
            if levelArray:
                resultArray.append(levelArray)
                levelArray = []             # clear the level array for next level
        
        return resultArray


        