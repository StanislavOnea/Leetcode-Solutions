from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        decrease = 0
        increase = 0
        ans = 0

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                increase += 1
                decrease = 0
            elif nums[i - 1] > nums[i]:
                increase = 0
                decrease += 1
            else:
                decrease = 0
                increase = 0

            ans = max(increase, ans, decrease)

        return ans + 1
