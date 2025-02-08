from typing import List
from collections import heapq


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
