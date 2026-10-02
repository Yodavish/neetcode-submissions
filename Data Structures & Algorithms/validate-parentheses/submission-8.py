class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '[' : ']',
            '{' : '}',
            '(' : ')'
        }

        stack = []
        for b in s:
            if b in brackets:
                stack.append(brackets[b])
            elif stack and stack[-1] == b:
                stack.pop()
            else:
                return False
        
        return stack == []