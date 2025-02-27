from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        set_nums = set(arr)
        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                t1, t2 = arr[i], arr[j]
                curr = 2
                while t1 + t2 in set_nums:
                    curr += 1
                    t1, t2 = t2, t1 + t2
                if curr > 2: 
                    ans = max(ans, curr)

        return ans
