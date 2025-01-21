from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        first = sum(grid[0]) - grid[0][0] 
        second = 0

        robot1 = 0
        robot2 = first

        for i in range(1, len(grid[0])):
            first -= grid[0][i]
            second += grid[1][i - 1]

            robot1 = max(first, second)
            robot2 = min(robot2, robot1)
        return robot2
