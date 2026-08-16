# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Solution 2: using level order traversal (BFS)

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        hashmap = {}
        queue = deque()
        queue.append((root, 0))         # (node, level)

        while queue:
            currentNode, level = queue.popleft()

            # Rightmost node at this level will overwrite previous nodes
            hashmap[level] = currentNode.val

            if currentNode.left:
                queue.append((currentNode.left, level + 1))
            if currentNode.right:
                queue.append((currentNode.right, level + 1))
                
        return list(hashmap.values())

        