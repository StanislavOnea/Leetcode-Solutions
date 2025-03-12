# Intuition
Brute force would be to traverse the array and check for negative and positive numbers and return max. Optimal aproach involves binary search since it's a sorted array.
# Approach
We need 2 binary searches one for finding the last negative number and one for finding first positive. Since we don't know how many 0's are there we cannot just skip them with a loop.

# Complexity
- Time complexity:
$$O(log(n))$$ - there 2 binary searches not nested so time complexity remains O(log(n)).

- Space complexity:
$$O(1)$$ - do not store additional collection

# Code
```python3 []
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = 0
        pos = 0
        for num in nums:
            if num < 0:
                neg += 1
            elif num > 0:
                pos += 1
        return max(pos, neg)

```