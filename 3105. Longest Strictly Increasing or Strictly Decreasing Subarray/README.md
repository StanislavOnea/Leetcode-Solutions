# Intuition
Just iterate trough list and calculate increasisn or decreasing subbarrays len. 
# Approach
Foe increasing and decreasing we use 2 variables that icremente when  find a certain sequence, if it's incresing sequence increse counter of inc and reset dec counter. At each step store maximum.

# Complexity
- Time complexity:
O(n)

- Space complexity:
O(1)

# Code
```python3 []
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        decrease = 0
        increase = 0
        ans = 0

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                increase += 1
                decrease = 0
            elif nums[i - 1] > nums[i]:
                increase = 0
                decrease += 1
            else:
                decrease = 0
                increase = 0

            ans = max(increase, ans, decrease)

        return ans + 1
    
```