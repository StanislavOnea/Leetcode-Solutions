# Intuition
The description is a bit uncler but basically we should find for every cell distances for the nearest "water cell".

# Approach
Use bfs starting with each water cell and update the distance.

# Complexity
- Time complexity:
O(nm) - we should modify every cell

- Space complexity:
O(nm) - the size of the deque in wors case.

# Code
First aproach:
```python3 []
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n = len(isWater)
        m = len(isWater[0])
        ans = [[-1] * m for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    ans[i][j] = 0
                    q.append((i, j))
        
        while q:
            i, j = q.popleft()
            for ni, nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0 <= ni < n and 0 <= nj < m and ans[ni][nj] == -1:
                    ans[ni][nj] = ans[i][j] + 1
                    q.append((ni, nj))
                    
        return ans
                
```
