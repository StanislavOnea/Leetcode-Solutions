from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        even_count = 0
        odd_count = 0
        total_odd_subarrays = 0
        
        for num in arr:
            if num % 2 == 0:
                even_count += 1
            else:
                even_count, odd_count = odd_count, even_count
                odd_count += 1
            
            total_odd_subarrays = (total_odd_subarrays + odd_count) % MOD
        
        return total_odd_subarrays
