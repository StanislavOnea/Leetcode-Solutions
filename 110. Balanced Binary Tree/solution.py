from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 1

            left = dfs(node.left)
            right = dfs(node.right)

            if not left or not right:
                return 0

            if abs(left - right) > 1:
                return 0
            
            return 1 + max(left, right)

        res = dfs(root)
        return True if res else False           
