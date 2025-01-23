# Intuition
Use dfs and keep max dpeth of left and right.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(n)

# Code
```python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        def dfs(node):
            nonlocal max_diameter
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            max_diameter = max(max_diameter, left + right)
            
            return 1 + max(left, right)

        dfs(root)
        return max_diameter

```