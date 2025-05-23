# Intuition
Wr should extract the groups from nums which are in the same limit.

# Approach
Sort by value to be able to create groups of the same limit range. We need groups to be able to know which nums we can swap. After createing groups we should check if nums with greater value are having less index if not we should do so. So I created a sorted list of values and idexes and assigned tha max value with the min index since all teh nums in group can be swaped because their are in the same limit.

# Complexity
- Time complexity:
O(nlog(n)) - the main complexity is sorting.
- Space complexity:
O(n) - we keep track of all nums in groups.

# Code
```python3 []
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        indices = [(num, i) for i, num in enumerate(nums)]
        indices.sort()

        groups = []
        group = [indices[0]]
        for r in range(1, len(indices)):
            if indices[r][0] - group[-1][0] <= limit:
                group.append(indices[r])
            else:
                groups.append(group)
                group = [indices[r]]

        groups.append(group)
        for g in groups:
            sorted_idx = sorted(g, key=lambda x: x[1])
            for i, val in zip(sorted_idx, g):
                nums[i[1]] = val[0]


        return nums

```