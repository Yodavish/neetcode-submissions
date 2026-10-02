class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '[' : ']',
            '{' : '}',
            '(' : ')'
        }

        seen = []
        for bracket in s:
            if bracket in brackets:
                seen.append(brackets[bracket]) 
            elif not seen:
                return False 
            else:
                b = seen.pop()
                if b != bracket:
                    return False

        return len(seen) == 0