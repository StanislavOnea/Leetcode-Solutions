# Intuition
Backtrack and find all possible permutations.

# Approach
Use counter for how many characters we can use. At each step iterate trough counter and use available characters. Add the res 1 each time, the posibility of using a sequence without any other characters.

# Complexity
- Time complexity:
O(!k) - k distinct chars

- Space complexity:
O(n) - for stack of backtracking

# Code
```python3 []
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        letters = Counter(tiles)
        
        def backtracking():
            ans = 0
            
            for x, count in letters.items():
                if count > 0:
                    letters[x] -= 1
                    ans += 1
                    ans += backtracking()
                    letters[x] += 1
                    
            return ans
            
        return backtracking()
```
