# Intuition
Divide the problem into subproblems and use dp with tabulation.

# Approach
The subproblems would be the each substring from str1 starting form i with each substring from str2 starting from j. We can start from the least characters of each. Consider base case empty char at the end, so the subproblem for empty char with empty char is "" and so on subproblem for empty char of str1 with last char of str2 would be last chr of str2. Thats why we have to hardcode these base subproblems in our dp grid the vombination of substring starting from that point with empty char. After we can compute starting with last chars of strings. If chars are the same we can add the char to result and concatenate the subproblem of i + 1, j + 1. If they are not the same we have to choce so we take str1[j] and check if we add this then we need the subproblem of i + 1, j if we chose str2[j] then we should concatenate str2[j] with subprolem of i, j + 1 and we do so until dp[0][0]. Since we use only 2 rows for chossing (diagonal, down, right) we don't need the entire grid for that and we can use 2 lists and change new computed list to be the next old list.

# Complexity
- Time complexity:
$$O(n * m * (n + m))$$ - O(n * m) for outer and inner loop O(n + m) for string concatenation inside those loops.

- Space complexity:
$$O(m ⋅(n+m))$$ - (n+m) for max possible string and m for len of a column.

# Code
```python3 []
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        old = [str2[i:] for i in range(m + 1)]

        for i in range(n - 1, -1, -1):
            new = [""] * (m + 1)
            new[-1] = str1[i:]

            for j in range(m - 1, -1, -1):
                if str1[i] == str2[j]:
                    new[j] = str1[i] + old[j + 1]
                elif len(new[j + 1]) <= len(old[j]):
                    new[j] = str2[j] + new[j + 1]
                else:
                    new[j] = str1[i] + old[j]

            old = new
                

        return old[0]

```