# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        resultArray = []
        stack = []
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
                
                stack.append(currentNode.val)
            if stack:
                resultArray.append(stack)
            stack = []
        return resultArray
        