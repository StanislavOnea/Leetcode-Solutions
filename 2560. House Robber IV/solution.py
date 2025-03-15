from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def is_valid_capability(cap):
            i = 0
            count = 0
            while i < n:
                if nums[i] <= cap:
                    i += 2
                    count += 1
                else:
                    i += 1

                if count == k:
                    return True
            
            return False

        l = min(nums)
        r = max(nums)

        while l <= r:
            mid = l + (r - l) // 2

            if is_valid_capability(mid):
                r = mid - 1
            else:
                l = mid + 1

        return l
