#2300. Successful Pairs of Spells and Potions

import math

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        def searchMinSuccessfulIndexInPotions(successfulValue: int):
            l, r = 0, len(potions)
            p = r//2

            while r > l:
                if potions[p] >= successfulValue:
                    r = p
                else:
                    l = p + 1
                p = (r + l) // 2
            return p

        numberOfSuccess = list()
        for i in range(0, len(spells)):
            currentMinSuccess = math.ceil(success/spells[i])
            print(currentMinSuccess)
            numberOfSuccess.append(len(potions) - searchMinSuccessfulIndexInPotions(currentMinSuccess))

        return numberOfSuccess
