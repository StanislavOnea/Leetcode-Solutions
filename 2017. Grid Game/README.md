# Intuition
First I thought to use DFS and just find the largest path and set values from path to 0. But after I understood that it can be solved with greedy min max aproach.

# Approach
We can see that the second robot will be able to choose between the upper right maximum values ​​or the lower left values, because at some point the first robot should turn once and then stop.
Using the prefix sums of each robot2 cell, the minimum of the first robot's choices will be chosen (since it will choose the highest ones).

# Complexity
- Time complexity:
O(n) where n is number of columns.

- Space complexity:
O(1) - we dont need to store a array of sums.

# Code
```python3 []
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

```