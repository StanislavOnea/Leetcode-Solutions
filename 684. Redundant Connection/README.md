# Intuition
It's clearly a graph problem where we should find a cycle. But the problem with standart DFS of BFS solution is to actually return the last edge that creates that cycle so this is a good problem to understand and use Union-Find.

# Approach
We should set the parent of each node as the root parent. A node may be not connected directly to the root parent but trough a series of other nodes. If we indetify 2 nodes with the same root parent that means there is a cycle. So we set the root parent of each node and ion moment that we found that parent is the same that means we created a cycle adding thes edge it means we should return this edge.
# Complexity
- Time complexity:
O(n) - unionm operation is very fast so we can consider it as O(1) sow e should iterate over the input edges.
- Space complexity:
O(n) - we store 2 arrays of nodes and root parent and also parents with their rank (number of nodes) to identify the root nodes (most populated).

# Code
```python3 []
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]

        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] >= rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
            
        for i, j in edges:
               if not union(i, j):
                return [i, j]
        
```