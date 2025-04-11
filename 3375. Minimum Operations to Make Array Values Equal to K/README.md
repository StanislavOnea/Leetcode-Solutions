# Intuition
Find all unique numbers greater than k. That would be the answer. If there is a num less than k then return -1.

# Approach
Using a set keep only unique occurances of nums. If the number is greater than k icrement response if less then return -1 directly.

# Complexity
- Time complexity:
$$O(n)$$ - iteration

- Space complexity:
$$O(n)$$ - for set

# Code
```python3 []
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        unique_nums = set(nums)
        res = 0

        for num in unique_nums:
            if num > k:
                res += 1
            if num < k:
                return -1

        return res
        
```