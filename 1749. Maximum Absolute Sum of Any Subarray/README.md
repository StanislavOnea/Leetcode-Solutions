# Intuition
Keep track of min prefix sum and max prefix sum. If min or max passes 0 in any directions reset the counter.

# Approach
2 variables for min and max, to store prefixes with max value, in case the current num is greater than max or smaller than 0 reset counter to current num.

# Complexity
- Time complexity:
$$O(n)$$ - for traversal.

- Space complexity:
$$O(1)$$ - no need for extra space.

# Code
```python3 []
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_so_far = 0
        min_so_far = 0
        max_ending_here = 0
        min_ending_here = 0
        
        for num in nums:
            max_ending_here = max(max_ending_here + num, num)
            max_so_far = max(max_so_far, max_ending_here)
            
            min_ending_here = min(min_ending_here + num, num)
            min_so_far = min(min_so_far, min_ending_here)
        
        return max(max_so_far, abs(min_so_far))

```