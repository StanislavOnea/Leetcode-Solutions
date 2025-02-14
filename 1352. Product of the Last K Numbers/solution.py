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
