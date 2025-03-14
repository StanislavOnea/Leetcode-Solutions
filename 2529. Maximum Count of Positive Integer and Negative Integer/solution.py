from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def nr_of_piles(n):
            res = 0
            for candy in candies:
                res += candy // n
            return res              

        sum_candy = sum(candies)
        if sum_candy < k:
            return 0
        r = sum_candy // k
        l = 1

        while l <= r:
            mid = (l + r) // 2
            piles = nr_of_piles(mid)

            if piles >= k:
                l = mid + 1
            else:
                r = mid - 1

        return r
