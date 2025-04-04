from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        deepest_leaves = []

        while q:
            deepest_leaves = list(q)
            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        def lowestCommonAncestor(root, p, q):
            if not root:
                return None

            if root == p or root == q:
                return root

            left_lca = lowestCommonAncestor(root.left, p, q)
            right_lca = lowestCommonAncestor(root.right, p, q)

            if left_lca and right_lca:
                return root
            
            if left_lca:
                return left_lca
            
            return right_lca

        
        return lowestCommonAncestor(root, deepest_leaves[0], deepest_leaves[-1])

    