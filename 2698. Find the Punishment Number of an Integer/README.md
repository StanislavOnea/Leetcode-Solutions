# Intuition
Cumpute each partition of the number. Try to add all the possibilities and if it's equal to our i then add the square root to the res.
# Approach
Used num as string for partition. At each point we chose to add the current partition and compute new ones or go further and add digits to this partition. Return True only if we used all the digits and the sum is equal to i.

# Complexity
- Time complexity:
$$O(n \cdot 2^{\log^2 n})$$ - because the square root can have at most $$O(\log^2 n)$$ digits and backtracking adds exponential complexity.

- Space complexity:
$$O(\log^2 n)$$ - maximum number of digits.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->


# Code
```python3 []
class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        def dfs(l, r, num, total):
            if l == len(s) and total == num:
                return True
            if r >= len(s) or total > num:
                return False
            
            add = dfs(r + 1, r + 1, num, total + int(s[l: r + 1]))
            cont = dfs(l, r + 1, num, total)

            return add or cont

        res = 0
        for i in range(1, n + 1):
            s = str(i * i)

            if dfs(0, 0, i, 0):
                res += i * i
        
        return res

``` 