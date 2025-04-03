# Intuition
Check for maximul possible difference so far until this point(not included) and mutliply with current number to update max answer so far.

# Approach
Use 3 variables 1 for max_value we will subtract from it every time to find max_diff. Update at each point max_re which will store to potential maximum response.

# Complexity
- Time complexity:
$$O(n)$$ - iteration

- Space complexity:
$$O(1)$$ - no additional space

# Code
```python3 []
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_diff = 0
        max_val = 0
        max_res = 0
        
        for num in nums:
            max_res = max(max_res, max_diff * num)
            max_diff = max(max_diff, max_val - num)
            max_val = max(max_val, num)
        
        return max_res if max_res > 0 else 0

```