# Intuition
Use dfs or bfs to compute the tree. FOr find just keep the values in a set.

# Approach
Compute the tree with right values using traversing such as bfs or dfs. Fin find when computing the tree store the values in the set and when find call check the existence of target in set.

# Complexity
- Time complexity:
$$O(n)$$ - for constructor.
$$O(1)$$ - for find.

- Space complexity:
$$O(n)$$ - keeping values in set.

# Code
```python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.seen = set()
        self._dfs(self.root, 0)
        

    def find(self, target: int) -> bool:
        return target in self.seen

    def _dfs(self, node, val):
        if not node:
            return

        node.val = val
        self.seen.add(val)
        self._dfs(node.right, 2 * val + 2)
        self._dfs(node.left, 2 * val + 1)

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
```