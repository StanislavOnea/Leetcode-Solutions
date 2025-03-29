# Intuition
Calcualte score for each entry. Calculate how many subarrays with this num we can use given that we know the score. Sort the array to use bigger numbers first until hit k. We can use a number that many times that we have subarrays where it have dominant score.

# Approach
Implement a calculation score for numbers. We can check from 2 first primary number how many of the primary numbers can divide the n (the function works for primary because for example 4 whil not have % == 0 because we divided all 2s before) store only distinct numbers.
After having the scores we can check from the left where ar the first number with score greater than current score and from the right the same. Having that information we can count subarrays where current numbers have max score:
(i - left[i] + 1) * (right[i] - i + 1)
it's the number of how much times we can use this number for the result.
Sort the array to use largest nums first. Multiply our res starting with 1 that many times that we calculated before and move to next num until max nr of operations is hit.



# Complexity
- Time complexity:
$$O(n log n + n * sqrt(m))$$ - biggest parts are the sorting nlogn but also calculation the score with our funciton  n * sqrt(m) where m is the max number from array.

- Space complexity:
$$O(n)$$ - for additional lists

# Code
```python3 []
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

```