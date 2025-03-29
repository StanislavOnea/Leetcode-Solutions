from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        def calculate_score(n):
            score = 0
            i = 2
            while i * i <= n:
                if n % i == 0:
                    score += 1
                    while n % i == 0:
                        n //= i
                i += 1
            if n > 1:
                score += 1
            return score
        
        scores = [calculate_score(num) for num in nums]
        
        left = [0] * n
        right = [n-1] * n
        
        stack = []
        for i in range(n):
            while stack and scores[stack[-1]] < scores[i]:
                stack.pop()
            left[i] = stack[-1] + 1 if stack else 0
            stack.append(i)
        
        stack = []
        for i in range(n-1, -1, -1):
            while stack and scores[stack[-1]] <= scores[i]:
                stack.pop()
            right[i] = stack[-1] - 1 if stack else n-1
            stack.append(i)
        
        contribution = [(i - left[i] + 1) * (right[i] - i + 1) for i in range(n)]
        
        elements = [(nums[i], contribution[i]) for i in range(n)]
        elements.sort(reverse=True)
        
        result = 1
        for num, count in elements:
            operations = min(count, k)
            result = (result * pow(num, operations, MOD)) % MOD
            k -= operations
            if k == 0:
                break
        
        return result
