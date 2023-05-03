from math import log

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            return round(log(n , 4), 9) % 1 == 0