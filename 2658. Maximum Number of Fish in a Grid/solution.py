from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0
            if grid[i][j] == 0 or (i, j) in visited:
                return 0
            
            visited.add((i, j))

            d = dfs(i + 1, j)
            u = dfs(i - 1, j)
            r = dfs(i, j + 1)
            l = dfs(i, j - 1)

            return grid[i][j] + d + u + r + l
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    ans = max(ans, dfs(i, j))

        return ans
