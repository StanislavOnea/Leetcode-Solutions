from typing import List


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
