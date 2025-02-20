# Intuition
Brute force:
Transform binary string in int and iterate until max int possible given len until we find a missing int.
Optimal:
Cantor’s Diagonal Argument. For each i in len(nums) we negate the bit on that position of a string from that index. So we can be sure that the new string will have at least 1 difference compared to all others.

# Approach
Brute force:
Tranform string in inte with int(s, 2), store all ints in a set. Iterate from 0 to max int possible (len(nums) of 1's). When finding first missing int convert it back to binary with "{i:0{len(nums)}b}" and return result.
Optimal:
For each string negate te char onf ith position. The logic is that we negate a char of each string we will have at least 1 bit difference between result and each string from array.

# Complexity
- Time complexity:
Brute force: $$O(2^n)$$ - due to max_num size.
Optimal: $$O(n)$$ - just iterate over array.

- Space complexity:
Brute force: $$O(n)$$ - due to set storage.
Optimal: $$O(1)$$ - no need for additional storage.

# Code
Brute force:
```python3 []
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        occur = set()

        for binary in nums:
            occur.add(int(binary, 2))

        max_num = "1" * len(nums)
        max_num = int(max_num, 2)

        for i in range(max_num + 1):
            if i not in occur:
                return f"{i:0{len(nums)}b}" 

        return -1

```

Optimal:
```python3 []
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return "".join('1' if nums[i][i] == '0' else '0' for i in range(len(nums)))

```