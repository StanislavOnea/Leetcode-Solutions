# Intuition
I thought in tetms of sum algo where we would need the total sum and the prefixes to find a certain suffix of len(nums) - k. But with multiply is a bit more tricky because of mult with 0 that discard the whole total. So we have to start again every time when we find a 0.
# Approach
Compute prefixes, if we find a 0 then add it to prefixes at that position, memorize the index of 0 and wehn we continue to calculate total product iv prev prefix is 0 then we start again with 1. Returning the result just divide the last total prefix by the prefix of k'th element from the end. Keep in mind that if there is a 0 in the interval from last k'th to the end then the whole product should be 0.

# Complexity
- Time complexity:
O(1) - for the operations

- Space complexity:
O(n) - for storing prefixes.

# Code
```python3 []
class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]
        self.last_zero = -1
        

    def add(self, num: int) -> None:
        multiply = self.prefix[-1] if self.prefix[-1] != 0 else 1
        self.prefix.append(multiply * num)
        if num == 0:
            self.last_zero = len(self.prefix) - 1

    def getProduct(self, k: int) -> int:
        if self.last_zero != -1 and len(self.prefix) - k-1 < self.last_zero:
            return 0
        elif self.prefix[-k-1] == 0:
            return self.prefix[-1] // 1
        return self.prefix[-1] // self.prefix[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
```