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

        hashmap = {}            # stores level (key) : node value
        queue = deque()
        queue.append((root, 0))     # node, level number (starts with root (0))

        while queue:

            currentNode, currentLevel = queue.popleft()
            hashmap[currentLevel] = currentNode.val     

            if currentNode.left:
                queue.append((currentNode.left, currentLevel + 1))
            if currentNode.right:
                queue.append((currentNode.right, currentLevel + 1))   
        
        return list(hashmap.values())
            


        
        