from typing import List
from collections import heapq


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        count = 0

        for i in range(len(nums)):
            x = heapq.heappop(nums)
            if x >= k:
                return count
            y = heapq.heappop(nums)

            num = x * 2 + y
            count += 1
            heapq.heappush(nums, num)

        return count
