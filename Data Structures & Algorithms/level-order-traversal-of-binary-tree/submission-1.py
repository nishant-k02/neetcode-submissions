# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        temp = []
        final = []

        while queue:
            size = len(queue)

            for i in range(size):
                current = queue.popleft()
                temp.append(current.val)
                
                if current.left:
                    queue.append(current.left)

                if current.right: 
                    queue.append(current.right)            

            if temp:
                final.append(temp)
            temp = []
        return final  