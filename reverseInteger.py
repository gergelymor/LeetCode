#7. Reverse Integer
# Python 3

class Solution:
    def reverse(self, x: int) -> int:
        stringValue = str(x)
        intValueReversed = stringValue[::-1]
        if stringValue[0] == "-":
            intValueReversed = "-" + intValueReversed[:-1]
        ret = int(intValueReversed)
        if ret < -2**31 or ret > (2**31)-1:
            return 0
        return ret
