# Intuition
The intuition was to check edge cases and store a dict of current colors.

# Approach
Use 2 dictionaries for distinct colors and number of them and also for current coloer of the balls. If we replace the color of a ball and the current color of a ball is unique we should remove that color from colors dict. If the new color is unique and the color that it replaces is not unique (freq > 1) or is not 0 (not a color) then we add the color in colors dict and append to res if both current and new colors are unique we should decrement old color and increment for the new color so the answer remain the same.

# Complexity
- Time complexity:
O(n) - the len of queries.
- Space complexity:
O(n) - store the balls and colors from queries.

# Code
```python3 []
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = {}
        colors = Counter()
        res = []

        for x, y in queries:
            prev_color = balls.get(x, 0)
            if prev_color:
                colors[prev_color] -= 1
                if colors[prev_color] == 0:
                    colors.pop(prev_color)

            colors[y] += 1
            balls[x] = y
            res.append(len(colors))

        return res

```