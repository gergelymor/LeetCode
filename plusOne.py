#66. Plus One

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        reversed = digits[::-1]
        firstDigit = reversed[0]+1
        if len(reversed) == 1:
            return list(map(int, str(firstDigit)))
        resultReversed = str(firstDigit%10)
        overflow = 0 if firstDigit < 10 else 1
        for i in range(1,len(reversed)):
            number = reversed[i]+overflow
            if number > 9:
                overflow = 1
            else:
                overflow = 0
            resultReversed += str(number%10)
        if overflow == 1:
            resultReversed += "1"
        return list(resultReversed)[::-1]
