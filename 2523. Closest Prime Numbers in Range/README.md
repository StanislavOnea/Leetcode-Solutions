# Intuition
Use Sieve of Eratosthenes for computing primes and compute the difference between primes inside the left-right subarray.

 
# Approach
Compute using Sieve of Eratosthenes(for each prime number mark the index of all multiples until right as as not prime). Extract only the primes from left to right. Then for each consecutive primes calculate the difference it's less than current update the min difference and result.

# Complexity
- Time complexity:
$$O(n log log n)$$ - complexity of computing primes with sieve (n = right).

- Space complexity:
$$O(right)$$ - store all primes in a list

# Code
```python3 []
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        def sieve(n):
            is_prime = [True] * (n + 1)
            is_prime[0] = False
            is_prime[1] = False

            for i in range(2, int(n ** 0.5) + 1):
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False

            return is_prime

        is_prime = sieve(right)
        primes = [j for j in range(left, right + 1) if is_prime[j]]
        
        if len(primes) < 2:
            return [-1, -1]

        min_dist = float("inf")
        res = []
        for i in range(1, len(primes)):
            if primes[i] - primes[i - 1] < min_dist:
                min_dist = primes[i] - primes[i - 1]
                res = [primes[i - 1], primes[i]]

        return res

```