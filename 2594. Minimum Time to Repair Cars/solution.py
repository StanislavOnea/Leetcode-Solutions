from typing import List


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
    
