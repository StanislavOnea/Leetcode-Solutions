from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        non_zero_index = 0

        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            if nums[i] != 0:
                nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
                non_zero_index += 1

        return nums
