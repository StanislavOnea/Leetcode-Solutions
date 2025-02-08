# Intuition
The intuition was to use 2 dict one with mapping of indexes of a number and another with mappind of index -> number. We can use heaps for extracting the minimum since there could be many indexes for a number. But laso some indexes can be not valid anymore since the number was replaced with another. In that case we do not try to find it in heap and delete but will delete when we will try to retrieve min value (if needed).
# Approach
2 dict for index -> number and number -> indexes mappings. At change just populate those 2 maps. When try to find extract minimum an check if the index indeed reference given number if not delete and try again until will find the index that refere the number or retrun -1 if didn't find anything.

# Complexity
- Time complexity:
O(log N) - due to heap insertion.

- Space complexity:
O(N) - usage of the dicts.

# Code
```python3 []
class NumberContainers:

    def __init__(self):
        self.min_indexes = {}
        self.numbers = {}

    def change(self, index: int, number: int) -> None:
        self.numbers[index] = number
        if number not in self.min_indexes:
            self.min_indexes[number] = []
        heapq.heappush(self.min_indexes[number], index)

    def find(self, number: int) -> int:
        if number not in self.min_indexes or len(self.min_indexes[number]) < 1:
            return -1

        idx = heapq.heappop(self.min_indexes[number])
        while self.min_indexes[number] and idx in self.numbers and self.numbers[idx] != number: 
            idx = heapq.heappop(self.min_indexes[number])
        if idx in self.numbers and self.numbers[idx] == number:
            heapq.heappush(self.min_indexes[number], idx)
            return idx
        
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
```