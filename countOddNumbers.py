#1523. Count Odd Numbers in an Interval Range

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if (high-low+1) % 2 == 0:
            return (high-low+1)//2
        else:
            if high % 2 != 0:
                return ((high-low)//2)+1
            else:
                return (high-low)//2
