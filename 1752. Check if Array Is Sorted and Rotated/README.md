# Intuition
Intuiton was to check if there are a point where nums[i - 1] > nums[i] there should be the rotation. If there is no such point than it's just sorted without rotation if there are 2 or more such points it means it's not sorted and rotated. Also we have to check after finding the rotation point if the second part of the array is also sorted starting from last number from first half.
# Approach
Find the index of rotation and check starting from that index until that index that the array is in sorted order.

# Complexity
- Time complexity:
O(n) - iterate list.

- Space complexity:
O(1) - no additional space.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        idx = 0
        prev = 0

        for i in range(len(nums)):
            if prev > nums[i]:
                count += 1
                idx = i

            if count > 1:
                return False
            prev = nums[i]

        for i in range(idx):
            if prev > nums[i]:
                count += 1
                idx = i

            if count > 1:
                return False
            prev = nums[i]

        return True

```