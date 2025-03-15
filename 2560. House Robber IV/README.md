# Intuition
Check every possible answer if it can be true. The min capability can be min(nums) and the max cap max(nums). So try capabilities from min to max and return the lowest which is true. To optimize use binary search.


# Approach
For each possible capability check if its a possible answer which means there are at least k numbers <= to our potential answer. Keep checking with BS if return True that means we have a valid answer and can try a lower cap, if we have false then we sould try higher cap etc.

# Complexity
- Time complexity:
$$O(nlog(m))$$ - where m is a range between min(nums) and max(nums).

- Space complexity:
$$O(1)$$ - no additional space.

# Code
```python3 []
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def is_valid_capability(cap):
            i = 0
            count = 0
            while i < n:
                if nums[i] <= cap:
                    i += 2
                    count += 1
                else:
                    i += 1

                if count == k:
                    return True
            
            return False

        l = min(nums)
        r = max(nums)

        while l <= r:
            mid = l + (r - l) // 2

            if is_valid_capability(mid):
                r = mid - 1
            else:
                l = mid + 1

        return l

```