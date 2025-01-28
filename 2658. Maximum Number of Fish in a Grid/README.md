# Intuition
I thought that this problem is similar with Number of Islands. Basically we should find all lakes(water cell) and count the nr of fish in such a lake.

# Approach
From every water cell traverse all other water cells and store the sum of fish. Keep an variable to find the most populated "lake" and return it. Don't forget to mark visited cells.

# Complexity
- Time complexity:
O(n * m) - in worst case we will have to traverse the whole grid.

- Space complexity:
O(n * m) - necessary for dfs.

# Code
```python3 []
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

```