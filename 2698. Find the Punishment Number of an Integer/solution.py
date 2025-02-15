from typing import List


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
