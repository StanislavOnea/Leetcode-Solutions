# Intuition
We want to find a number that would be the most suitable for both numbers that are bigger and that are less so we have to find the median an try to equal all numbers to that. If our x after few operation cannot exactly mutch the median then we cannot meet the requirements.
# Approach
Flaten the matrix and sort for finding median. For each number in the flatten array check how many operation should we perform to match median and add to response. If dividing the remaining part betwenn medain and number would result is a non natural number then we cannot meet the requirements.

# Complexity
- Time complexity:
$$O(m * n log(m * n))$$ - complexity cames from sorting the flatten array which is of size m * n.

- Space complexity:
- $$O(n * m)$$ - for flaten array 

# Code
```python3 []
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
    
```