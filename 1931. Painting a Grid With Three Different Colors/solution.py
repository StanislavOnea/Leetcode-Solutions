from itertools import product

class Solution:
    def compare(self, s1, s2):
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                return False
        return True
    
    def colorTheGrid(self, m: int, n: int) -> int:
        rows = n
        cols = m
        mod = 10 ** 9 + 7

        possible = ['0', '1', '2']
        single_row = set()

        for p in product(possible, repeat=cols):
            if all(p[i] != p[i+1] for i in range(cols - 1)):
                single_row.add(''.join(p))

        memo = {}
        def dp(curr, prev):
            key = (curr, prev)
            if key in memo:
                return memo[key]
            if curr >= rows:
                return 1
            
            res = 0
            for r in single_row:
                if not prev:
                    res += dp(curr + 1, r)
                else:
                    satisfy = self.compare(prev, r)
                    res += dp(curr + 1, r) if satisfy else 0
            
            memo[key] = res % mod
            return res % mod
        
        return dp(0, None) % mod
