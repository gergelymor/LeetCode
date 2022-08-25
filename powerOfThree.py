#326. Power of Three

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n/3 > 2:
            n=n/3
        if n == 1 or n == 3:
            return True
        else:
            return False
            
        
