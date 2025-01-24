# Intuition
Intuition was topological sort. The nodes that have only "in" connection are the end nodes the ones that have cicles may be connected to end nodes but are also connected to other nodes.

# Approach
For each node check if its a terminal node or is connected to a terminal node then add to response. If node is a part of a cycle don't include in response.

# Complexity
- Time complexity:
O(n) - we should visit with dfs all the nodes.

- Space complexity:
O(n) - wee keep information of terminal nodes.

# Code
```python3 []
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = set()
        memo = [0] * len(graph)
        def dfs(i):
            nonlocal memo
            if len(graph[i]) == 0 or memo[i] == 1:
                return True
            if memo[i] == -1 or i in visited:
                return False

            visited.add(i)
            for nei in graph[i]:
                if not dfs(nei):
                    memo[i] = -1
                    memo[nei] = -1
                    return False

            memo[i] = 1
            return True
            
        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)

        return res

```