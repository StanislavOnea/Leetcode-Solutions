# Intuition
First thought was to use binary search and try different number of candies offered to children. We can also calculate the number of piles after dividing them so piles would have n candies.

# Approach
We can define that if the sum of candies are less than number of children then we cannot divide it. After that we define a function that calculats the number of piles with min n candies. So we devide the number of candies in a pile by n (if n = 3 and piles[i] == 6 then we can create 2 piles from it if piles[i] == 5 then only 1). Then we continue with binary search. Using our function we can find the nr of piles so if we have too much piles then we try to allocate more candies to children else we try to allocate less. Return the right boundry(since we want max candies).

An optimization the intial boundry of r as sum_candy // k since maximum possible candies to allocate are then when we can get rid of all candies (example [5, 5, 6] k = 3 max are 16 // 3 = 5)

# Complexity
- Time complexity:
$$O(nlog(n))$$ - the function is O(n) aand BS is log(n)

- Space complexity:
$$O(1)$$ - no additional space

# Code
```python3 []
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def nr_of_piles(n):
            res = 0
            for candy in candies:
                res += candy // n
            return res              

        sum_candy = sum(candies)
        if sum_candy < k:
            return 0
        r = sum_candy // k
        l = 1

        while l <= r:
            mid = (l + r) // 2
            piles = nr_of_piles(mid)

            if piles >= k:
                l = mid + 1
            else:
                r = mid - 1

        return r
            
```