from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_diff = 0
        max_val = 0
        max_res = 0
        
        for num in nums:
            max_res = max(max_res, max_diff * num)
            max_diff = max(max_diff, max_val - num)
            max_val = max(max_val, num)
        
        return max_res if max_res > 0 else 0
