from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_so_far = 0
        min_so_far = 0
        max_ending_here = 0
        min_ending_here = 0
        
        for num in nums:
            max_ending_here = max(max_ending_here + num, num)
            max_so_far = max(max_so_far, max_ending_here)
            
            min_ending_here = min(min_ending_here + num, num)
            min_so_far = min(min_so_far, min_ending_here)
        
        return max(max_so_far, abs(min_so_far))
