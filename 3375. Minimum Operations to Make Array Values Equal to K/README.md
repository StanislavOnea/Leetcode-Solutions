# Intuition
The problem is about intervals. We can check if there are more than 1 non overlapping intervals then we can split it. We should the same for both oX axis and oY axis.

# Approach
Split x and y axis and create list with intervals. Perform merge of those intervals. Check if there are at least 2 intervals that do not overlap in either ox or oy if so return True if not return False.

# Complexity
- Time complexity:
$$O(n)$$ - traversal

- Space complexity:
$$O(n)$$ - storing additional lists

# Code
```python3 []
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        ox = []
        oy = []
        for sx, sy, ex, ey in rectangles:
            ox.append([sx, ex])
            oy.append([sy, ey])

        ox.sort()
        oy.sort()
        merged_ox = []
        merged_oy = []

        for i in range(len(ox)):
            s = ox[i][0]
            e = ox[i][1]
            if not merged_ox:
                merged_ox.append([s, e])
                continue
            
            if merged_ox[-1][1] > s:
                last = merged_ox.pop()
                merged_ox.append([last[0], max(e, last[1])])
            else:
                merged_ox.append([s, e])

        for i in range(len(oy)):
            s = oy[i][0]
            e = oy[i][1]
            if not merged_oy:
                merged_oy.append([s, e])
                continue
            
            if merged_oy[-1][1] > s:
                last = merged_oy.pop()
                merged_oy.append([last[0], max(e, last[1])])
            else:
                merged_oy.append([s, e])

        not_overlapping_x = 0
        not_overlapping_y = 0
        for i in range(1, len(merged_ox)):
            if merged_ox[i - 1][1] <= merged_ox[i][0]:
                not_overlapping_x += 1
            
            if not_overlapping_x == 2:
                return True

        for i in range(1, len(merged_oy)):
            if merged_oy[i - 1][1] <= merged_oy[i][0]:
                not_overlapping_y += 1
            
            if not_overlapping_y == 2:
                return True
        
        return False

```