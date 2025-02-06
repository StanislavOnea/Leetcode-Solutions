# Intuition
Ituition was to use math for each sum with occurance greater than 1.

# Approach
We compute and store the frequency of sum of each 2 numbers.
And then we have to find to formula. So for 2 pairs with the same sum there are 8 permutations. So each pair have 2 permutations a, b and b, a and also the second pairs so it at least 4 permutations in total. After that we can just swap the pairs and we receive 8. What should we do when we have more than 2 pairs. In case of 3 pairs than we can think that we can substite a pair from previous 8 and we would recive 8 more for for [a, b, c, d] we can add [z, y, c, d] and [z, y, a, b] so we receive 24. Given this the formula is 8 * v * (v-1) // 2 where v is the frequence of that sum.

# Complexity
- Time complexity:
O(n^2) - we have to compute every possible pair.
- Space complexity:
O(n^2) - we have to store the occurances.

# Code
```python3 []
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                freq[nums[i] * nums[j]] += 1

        res = 0
        for k, v in freq.items():
            if v > 1:
                res+= 8 * v * (v-1) // 2

        return res
    
```