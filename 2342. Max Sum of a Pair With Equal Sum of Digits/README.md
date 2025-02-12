# Intuition
The intuition was to save the top 2 max values for each digit_sum in the array.
# Approach
Use a dict for mapping digit_sum for each number in nums. Store only the top 2 max numbers since we are interested in finding max sum of those nums. At each step update our response variable with max of two numbers.

# Complexity
- Time complexity:
O(n) - the traversal if nums. Sum digits is constant time since it will iterate maximum 10 times (10^9).
- Space complexity:
O(n) - for dictionary.

# Code
```python3 []
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sum_digits(num):
            s = 0
            while num != 0:
                s += num % 10
                num //= 10
            return s
            
        groups = {}
        ans = -1
        for i in range(len(nums)):
            sm = sum_digits(nums[i])
            if sm not in groups:
                groups[sm] = [nums[i], -1] 
            else:
                if nums[i] > groups[sm][0]:
                    groups[sm][0], groups[sm][1] = nums[i], groups[sm][0]
                elif nums[i] > groups[sm][1]:
                    groups[sm][1] = nums[i]

                if groups[sm][1] != -1:
                    ans = max(ans, groups[sm][0] + groups[sm][1])

        return ans

```