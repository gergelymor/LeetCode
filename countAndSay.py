#38. Count and say

class Solution:
    def countAndSay(self, n: int) -> str:
        ret = "1"
        if n == 1:
            return ret
        
        def say(num: str) -> str:
            if num == "1":
                return "11"
            said = ""
            a,b = 0,1
            while b < len(num) + 1:
                if b < len(num) and num[a] == num[b]:
                    b = b + 1
                else:
                    said = said + str(b-a) + num[a]
                    a = b
                    b = b + 1
            return said
                
        
        for i in range(1, n):
            ret = say(ret)
        return ret
        
