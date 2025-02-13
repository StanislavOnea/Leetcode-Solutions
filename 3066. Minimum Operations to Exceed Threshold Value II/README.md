# Intuition
To extract 2 min numbers and then insert num = x * 2 + y back to the array until the condition is satisfied.

# Approach
Use a min heap for extracting min values. Extract x and y calculate the formula x * 2 + y and add the result to heap. Do su until the extracter value form heap is greater or equal to k.

# Complexity
- Time complexity:
O(logN) - beacuse of traversal and heap operation.

- Space complexity:
)(1) - since we use the same list for heap.

# Code
```python3 []
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        count = 0

        for i in range(len(nums)):
            x = heapq.heappop(nums)
            if x >= k:
                return count
            y = heapq.heappop(nums)

            num = x * 2 + y
            count += 1
            heapq.heappush(nums, num)

        return count

```