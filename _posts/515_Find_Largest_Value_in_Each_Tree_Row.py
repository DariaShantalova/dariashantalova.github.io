# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        level = deque([root])
        ans = []

        while level:
            max_val = float('-inf')
            for _ in range(len(level)):
                node = level.popleft()
                max_val = max(node.val, max_val)

                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            ans.append(max_val)
        return ans
        
