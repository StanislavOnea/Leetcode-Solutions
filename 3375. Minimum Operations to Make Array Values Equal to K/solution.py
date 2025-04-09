from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        unique_nums = set(nums)
        res = 0

        for num in unique_nums:
            if num > k:
                res += 1
            if num < k:
                return -1

        return res
