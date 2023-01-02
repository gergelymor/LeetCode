#441. Arranging Coins

class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        fullRows = 0
        while i <= n:
            n = n - i
            fullRows = fullRows + 1
            i = i + 1
        return fullRows
