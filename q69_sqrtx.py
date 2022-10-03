class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1 or x == 2:
            return 1
        
        for i in range(0, x):
            if i * i <= x and (i + 1) * (i + 1) > x:
                return i