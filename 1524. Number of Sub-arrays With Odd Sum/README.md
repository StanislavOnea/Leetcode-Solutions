# Intuition
We should use the property that if next num is even it won't change the parity of odd and even prefixes so we can just store one more even prefix.
In case it's odd the odd prefixes + this number will become even but thew odd ones will become even so we have to add old even number (prefixes that we already have) and also the number of even prefixs that become odd now.

# Approach
Store in variables odd and even counter and also a total odd counter for tracking previous odd subarrays. When we encounter even number just increase the even counter, when we have odd number we can add to total odd the even total so far and + 1 for the 1 len subarray.

# Complexity
- Time complexity:
$$O(n)$$ - for traversal.

- Space complexity:
$$O(1)$$ - no need for extra space.

# Code
```python3 []
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        even_count = 0
        odd_count = 0
        total_odd_subarrays = 0
        
        for num in arr:
            if num % 2 == 0:
                even_count += 1
            else:
                even_count, odd_count = odd_count, even_count
                odd_count += 1
            
            total_odd_subarrays = (total_odd_subarrays + odd_count) % MOD
        
        return total_odd_subarrays

```