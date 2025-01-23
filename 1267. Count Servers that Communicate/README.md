# Intuition
The intuition was to iterate trough the rows and check if there is at least 1 computer then the next one would be connected. And then iterate trough columns.

# Approach
Iterate trough each row if we find a connection mark the nodes as 2 so we would not add them again when iterating trough columns. Iterate trough columns and check if there are cells > 0 then there is a computer to connect but we are not adding it to res because we already did at rows iteration.

# Complexity
- Time complexity:
O(n) -  we iterate 2 time trough matrix but it's still the same complexity.

- Space complexity:
O(1) - we don't have to store the counter of rows or columns.

# Code
```python3 []
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

```