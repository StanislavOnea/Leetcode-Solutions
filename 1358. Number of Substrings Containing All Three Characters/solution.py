from collections import defaultdict

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
