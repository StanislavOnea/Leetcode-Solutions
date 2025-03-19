# Intuition
Simplify problem so always change left most pointer from 0 to 1 because we will not be able to do so after (when mid and right pointer can be converted from 0 to 1 later).

# Approach
We should keep these 3 pointers, I used l, m, r and iterate over array and every time nums[l] == 0 flip all 3 digits. Doing so we will either receive an array with al 1's or one of the last 2 elements would be 0.

# Complexity
- Time complexity:
$$O(n)$$ - iteration.

- Space complexity:
$$O(1)$$ - no additional data stored.

# Code
```python3 []
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        
        l, m, r = 0, 1, 2
        res = 0

        while l < (len(nums) - 2):
            if nums[l] == 0:
                nums[l] = 1 - nums[l]
                nums[m] = 1 - nums[m]
                nums[r] = 1 - nums[r]
                res += 1

            l += 1
            m += 1
            r += 1

        return res if nums[-1] == 1 and nums[-2] == 1 else -1

```