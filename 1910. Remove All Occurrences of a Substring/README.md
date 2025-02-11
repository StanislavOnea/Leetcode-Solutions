# Intuition
- Aproach 1: Ituition was to use something like a stack but with faster equal check so firstly I thought tho just construct the string and remove from it when we find part.
- Aproach 2: Is to use replace function and do so while we can find the "part" ins string.
# Approach
- Aproach 1: Declare intial string, add char by char and check last len(part) substring if it matches with part delete it and continue assembling the string.
- Aproach 2: Check while part is in s then replace directly in string the part with "" (1 at a time). Do so until no part in s.

# Complexity
- Time complexity:
- Aproach 1: O(N * M) where n is len of s and m len of part.
- Aproach 2: O(N * M)

- Space complexity:
- Aproach 1: O(N) since we store additional string.
- Aproach 2: O(1) we use input string for replacing so its constant time.

# Code
```python3  []
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        part_len = len(part)
        j = 0

        curr = ""
        for i in range(len(s)):
            
            curr += s[i]
            j += 1

            if j - part_len >= 0 and curr[j - part_len:] == part:
                curr = curr[:j - part_len]
                j = j - part_len

        if curr == part:
            return ""
        return curr
```


```python3 []
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, "",1)
        return s

```

