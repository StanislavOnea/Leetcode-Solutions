# Intuition
Find all connected components using dfs and then check if all vertexes from componentds are connected to each other.

# Approach
For each vertex find the component (connection of vertexes) of that  using DFS. After finding the entire component check all the vertexes if it is connected to all other vertexes and add to answer. 

# Complexity
- Time complexity:
$$O(V + E)$$ - traverse all vertexes and edges.

- Space complexity:
$$O(V + E)$$ - mapping, visited and dfs traversal space.

# Code
```python3 []
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        edge_mapping = defaultdict(list)

        for s, d in edges:
            edge_mapping[s].append(d)
            edge_mapping[d].append(s)

        def dfs(node):
            if node in visited:
                return []

            visited.add(node)
            res = [node]
            for nei in edge_mapping[node]:
                res = res + dfs(nei)

            return res

        visited = set()
        ans = 0
        for i in range(n):
            if i not in visited:
                component = dfs(i)
                if all(len(edge_mapping[edge]) == len(component) - 1 for edge in component):
                    ans += 1
        
        return ans

```