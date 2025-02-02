from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        idx = 0
        prev = 0

        for i in range(len(nums)):
            if prev > nums[i]:
                count += 1
                idx = i

            if count > 1:
                return False
            prev = nums[i]

        for i in range(idx):
            if prev > nums[i]:
                count += 1
                idx = i

            if count > 1:
                return False
            prev = nums[i]

        return True

