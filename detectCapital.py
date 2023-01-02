#520. Detect Capital

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        for i, char in enumerate(word):
            if char.isupper():
                if i>0 and len(word) > i+1 and word[i+1].islower():
                    return False
            elif char.islower():
                if len(word)>i+1 and word[i+1].isupper():
                    return False
        return True
