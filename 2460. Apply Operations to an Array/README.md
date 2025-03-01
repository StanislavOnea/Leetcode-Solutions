# Intuition
Apply the describe operations in the statement and then we can use basic algo for moving all zeros to end. But we can also do taht directly in first traversal first apply operations and then move the non-zero elements to start of array.

# Approach
Combine describet operations andmoving zeros to end in one for loop. Return modified array.

# Complexity
- Time complexity:
$$O(n)$$ - for traversal

- Space complexity:
$$O(1)$$ - no extra space in-place modifications.

# Code
```python3 []
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        non_zero_index = 0

        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            if nums[i] != 0:
                nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
                non_zero_index += 1

        return nums

```