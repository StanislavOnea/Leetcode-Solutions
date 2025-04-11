# Intuition
Compute prefix and sufix of left and right part of the potential number. Combine them to check if it eters in low < num < high. We can compute only 2 digits or 4 digits given the constrain.
# Approach
For all combination of digits compute the prefix as 1000 * a + 100 * b and suffix as 10 * c + d we cannot compute prefix with leading 0.
Then for each possible sum of 2 digits (max 9 + 9 = 18) check how many of combination of 2 digits matches in prefix and suffix array and add it only if it satisfyi the condition low <= num <= high.

# Complexity
- Time complexity:
$$O(1)$$ - fixed number of calculation for given constrain.

- Space complexity:
$$O(1)$$ - keep array of fixed len

# Code
```python3 []
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0

        for d in range(1, 10):
            num = d * 10 + d
            if low <= num <= high:
                count += 1

        prefix_by_sum = [[] for _ in range(19)]
        suffix_by_sum = [[] for _ in range(19)]

        for a in range(1, 10):
            for b in range(10):
                total = a + b
                prefix_by_sum[total].append(1000 * a + 100 * b)

        for c in range(10):
            for d in range(10):
                total = c + d
                suffix_by_sum[total].append(10 * c + d)

        for digit_sum in range(19):
            for prefix in prefix_by_sum[digit_sum]:
                for suffix in suffix_by_sum[digit_sum]:
                    num = prefix + suffix
                    if low <= num <= high:
                        count += 1

        return count

```