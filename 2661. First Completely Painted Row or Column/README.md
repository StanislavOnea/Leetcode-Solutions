# Intuition
Use hashmaps for storing indexes and as counters.

# Approach
Use dict for storing indexes i and j form mat. Then use a counter for each row and column and when this counter hits the length return the index of arr.

# Complexity
- Time complexity:
O(n * m) since we iterate trhough all o cells.

- Space complexity:
O(n * m) since we store indexes of all cells.

# Code
```python3 []
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        coordinates = {}

        for i in range(n):
            for j in range(m):
                coordinates[mat[i][j]] = (i, j)

        rows = defaultdict(int)
        cols = defaultdict(int)
        for i in range(len(arr)):
            mat_i, mat_j = coordinates[arr[i]]
            rows[mat_i] += 1
            cols[mat_j] += 1
            if rows[mat_i] == m or cols[mat_j] == n:
                return i

        return -1
    
```