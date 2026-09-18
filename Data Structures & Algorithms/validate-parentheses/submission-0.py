class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        closing_brackets = []
        for b in s:
            if b in brackets:
                closing_brackets.append(brackets[b])
            elif not closing_brackets or b != closing_brackets[-1]:
                return False
            else:
                closing_brackets.pop()
        
        return len(closing_brackets) == 0
