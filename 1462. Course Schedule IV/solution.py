from typing import List
from collections import defaultdict


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        connections = defaultdict(list)
        for a, b in prerequisites:
            connections[a].append(b)

        dp = [set() for i in range(numCourses)]
        def dfs(course):
            for neighbor in connections[course]:
                if neighbor not in dp[course]:
                    dp[course].add(neighbor)
                    dp[course].update(dfs(neighbor))
            
            return dp[course]

        for i in range(numCourses):
            dp[i] = dfs(i)

        res = []
        for a, b in queries:
            if b in dp[a]:
                res.append(True)
            else:
                res.append(False)

        return res
