#20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        for char in s:
            if char is '{':
                stack.append('{')
            elif char is '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append('}')
            elif char is '(':
                stack.append('(')
            elif char is ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(')')
            elif char is '[':
                stack.append('[')
            elif char is ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(']')
        return len(stack) is 0
            
