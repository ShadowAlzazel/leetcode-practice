from math import log

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # We use logs to  figure out if power of three, anything less than 0 is void as its outside domain
        if n <= 0:
            return False
        else:
            #print(round(log(n , 3), 9))
            return round(log(n , 3), 9) % 1 == 0

