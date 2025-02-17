from collections import Counter


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
