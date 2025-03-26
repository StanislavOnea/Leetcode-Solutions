from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        total_len = len(grid) * len(grid[0])
        h = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                h.append(grid[i][j])
        
        if len(h) <= 1:
            return 0
        h.sort()
        median = h[len(h) // 2]

        res = 0
        for num in h:
            if (num - median) % x != 0:
                return -1
            res += abs(num - median) // x

        return res
    