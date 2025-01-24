from typing import List


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
