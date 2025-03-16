# Intuition
The problem can be solved using BS. We can try each response form 1 minute to the worst possible case. If we find a valid possibility then try less minutes.
 
# Approach
Define a function then check if its enough k minutes to repair all cars using formula sqrt(minutes / rank[i]). Define a binary search from l to min(ranks) * cars * cars.

# Complexity
- Time complexity:
$$O(nlog(n))$$ - complexity of BS plus iterating array.

- Space complexity:
$$O(1)$$ - no additional space.

# Code
```python3 []
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def can_repair(minutes):
            nr_cars = 0
            for rank in ranks:
                nr_cars += int((minutes // rank) ** 0.5)
                if nr_cars >= cars:
                    return True

            return nr_cars >= cars
        
        l = 0
        r = min(ranks) * cars * cars
        while l <= r:
            mid = l + (r - l) // 2

            if can_repair(mid):
                r = mid - 1
            else:
                l = mid + 1
                

        return l
    
```