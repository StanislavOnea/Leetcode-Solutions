from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        
        l, m, r = 0, 1, 2
        res = 0

        while l < (len(nums) - 2):
            if nums[l] == 0:
                nums[l] = 1 - nums[l]
                nums[m] = 1 - nums[m]
                nums[r] = 1 - nums[r]
                res += 1

            l += 1
            m += 1
            r += 1

        return res if nums[-1] == 1 and nums[-2] == 1 else -1
