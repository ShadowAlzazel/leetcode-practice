class Solution:
    def integerBreak(self, n: int) -> int:
        # IDEAS: Find the primes!
        # 10 = 3 + 3 + 2 + 2
        # 11 = 3 + 3 + 3 + 2
        # If n % 3 = -> add 2 + 2 or 3?
        if n == 2:
            return 1
        elif n % 3 == 0:
            if n == 3:
                return 2
            return pow(3, n // 3)
        elif n % 3 == 1:
            return pow(3, (n // 3) - 1) * 4
        elif n % 3 == 2:
            return pow(3, n // 3) * 2