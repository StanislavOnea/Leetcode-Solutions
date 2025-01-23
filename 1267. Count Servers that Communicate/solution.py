from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            last = None
            for j in range(len(grid[0])):
                if grid[i][j] > 0 and last:
                    x, y = last
                    if grid[x][y] == 1:
                        grid[x][y] = 2
                        ans += 1
                    if grid[i][j] == 1:
                        grid[i][j] = 2
                        ans += 1

                if grid[i][j] > 0 and not last:
                    last = (i, j)

        for i in range(len(grid[0])):
            last = None
            for j in range(len(grid)):
                if grid[j][i] > 0 and last:
                    x, y = last
                    if grid[x][y] == 1:
                        grid[x][y] = 2
                        ans += 1
                    if grid[j][i] == 1:
                        grid[j][i] = 2
                        ans += 1

                if grid[j][i] > 0 and not last:
                    last = (j, i)

        return ans          
