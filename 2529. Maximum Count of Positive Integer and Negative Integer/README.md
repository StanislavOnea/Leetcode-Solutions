# Intuition
Use sliding window for finding all substring with a condition that involves at least.

# Approach
If all of the chars are in substring then add to res the number equal o all of chars after that substring (because they also satisfy the condition because at least a, b, c are in all of them). Shrink the window from the left until the condition is not met anymore continue to add to res since for "kabck" we need to consider "kabc" + all chars after, and also just "abc" and all chars after.

# Complexity
- Time complexity:
$$O(n)$$ - for traversal.

- Space complexity:
$$O(1)$$ - since the max len of dict can be 3 it's O(1) space complexity.

# Code
```python3 []
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        count = defaultdict(int)
        n = len(s)
        res = 0

        for r in range(n):
            if s[r] in "abc":
                count[s[r]] += 1
                
            while len(count) >= 3:
                if s[l] in count:
                    count[s[l]] -= 1

                    if count[s[l]] <= 0:
                        del count[s[l]]
                l += 1
                res += n - r

        return res

```