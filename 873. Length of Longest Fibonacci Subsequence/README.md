# Intuition
It's a bit similar with 3sum we have to chose 2 nums and check if there is in nums a num == num1 + num2. But also we should while loop to find seq not only 1 number.

# Approach
Chose 2 elements and then using while iterate until in the array exist a num1 + num2 element if the element exist update num1 = num2 and num2 = num1 + num2.

# Complexity
- Time complexity:
$$O(n^2logM)$$ - $$n^2$$ for nested iterations and logM if for the while loop that can go maximum to the max element of array. Since fibonacci increse exponentially it's log. 

- Space complexity:
 $$O(n)$$ - for the set

# Code
```python3 []
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        set_nums = set(arr)
        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                t1, t2 = arr[i], arr[j]
                curr = 2
                while t1 + t2 in set_nums:
                    curr += 1
                    t1, t2 = t2, t1 + t2
                if curr > 2: 
                    ans = max(ans, curr)

        return ans

```