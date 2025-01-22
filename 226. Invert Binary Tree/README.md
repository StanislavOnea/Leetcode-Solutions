# Intuition
Use dfs to calculte depth, at each step compare if depth of left and right are balanced.

# Approach
If at this point left and right are balanced return the dept of current branch else return 0 which is False. If at the end of bfs it return 0 then at some point 2 branches wasn't balanced.

# Complexity
- Time complexity:
O(n) - iterate through all the nodes.
- Space complexity:
O(n) - store all the nodes in stack.

# Code
```python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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

```