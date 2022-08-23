#58. Length of Last Word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        reversedStr = s[::-1]
        transformed = reversedStr.split()
        return len(transformed[0])
