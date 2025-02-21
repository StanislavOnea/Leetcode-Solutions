from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
