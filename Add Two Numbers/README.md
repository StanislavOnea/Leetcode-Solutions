# Intuition
My intuition was the following: if we follow the directions of the arrow then we can go for free costs but if we want to change direction (or we are forcced to) we should add 1 to the cost (weight) so I naturally thougt of Djiskstra to find minimal path by cost

We should also keep in mind that some of the fields may have different routes with different costs so we have to keep track of cost of each cell an update it when the new cost is lower.

# Approach
Using djikstra with min-heap for lower cost path.

- If the next path is in the direction of current cell cost remain the same
- If not cost is cost + 1
- Keep track of minimal cost in a separate matrix dist and update that matrix only if a better way is - found. It also helps for tracking visited nodes.

# Complexity
- Time complexity:
O(N * M * log(N * M))

Since we have to go trough all of the cells (N * M) but also add in the worst case all cells from grid to the min-heap log(N * M).

- Space complexity:
O(N*M)
The heap and the matrix for minimal cost both can contains maximum all the cells.

# Code
```python3 []
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
```