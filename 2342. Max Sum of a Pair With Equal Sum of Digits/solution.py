from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sum_digits(num):
            s = 0
            while num != 0:
                s += num % 10
                num //= 10
            return s
            
        groups = {}
        ans = -1
        for i in range(len(nums)):
            sm = sum_digits(nums[i])
            if sm not in groups:
                groups[sm] = [nums[i], -1] 
            else:
                if nums[i] > groups[sm][0]:
                    groups[sm][0], groups[sm][1] = nums[i], groups[sm][0]
                elif nums[i] > groups[sm][1]:
                    groups[sm][1] = nums[i]

                if groups[sm][1] != -1:
                    ans = max(ans, groups[sm][0] + groups[sm][1])

        return ans
