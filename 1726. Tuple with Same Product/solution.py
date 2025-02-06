from typing import List
from collections import defaultdict


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                freq[nums[i] * nums[j]] += 1

        res = 0
        for k, v in freq.items():
            if v > 1:
                res+= 8 * v * (v-1) // 2

        return res
             
