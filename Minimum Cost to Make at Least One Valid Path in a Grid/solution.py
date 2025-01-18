import heapq
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0
        h = [(0, 0, 0)]
        
        while h:
            cost, i, j = heapq.heappop(h)
            
            if cost > dist[i][j]:
                continue
                
            if i == n - 1 and j == m - 1:
                return cost
                
            for direction, x, y in [[1, 0, 1], [2, 0, -1], [3, 1, 0], [4, -1, 0]]:
                next_i, next_j = i + x, j + y
                
                if 0 <= next_i < n and 0 <= next_j < m:
                    new_cost = cost + (0 if grid[i][j] == direction else 1)
                    
                    if new_cost < dist[next_i][next_j]:
                        dist[next_i][next_j] = new_cost
                        heapq.heappush(h, (new_cost, next_i, next_j))
        
        return dist[n-1][m-1]
