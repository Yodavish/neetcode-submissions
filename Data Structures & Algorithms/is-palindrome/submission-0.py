class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = "".join([char for char in s if char.isalnum()])

        l = 0
        r = len(clean_text) - 1

        while l < r:
            if clean_text[l].lower() != clean_text[r].lower():
                return False
            
            l += 1
            r -= 1

        return True