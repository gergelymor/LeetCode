#28. Implement strStr()

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        elif len(needle) > len(haystack):
            return -1
        else:
            for i in range(0,len(haystack)):
                if haystack[i] == needle[0] and len(haystack)-i >= len(needle):
                    for j in range(0,len(needle)):
                        if haystack[i+j] != needle[j]:
                            break
                        if j == len(needle)-1:
                            return i
            return -1
            
