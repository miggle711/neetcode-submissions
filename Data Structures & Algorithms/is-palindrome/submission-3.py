class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()

        if len(s) == 0:
            return True

        l = 0 
        r = len(s) - 1
        while l < r:
            print(f"l: {l}, r: {r}, s[l]: {s[l]}, s[r]: {s[r]}")
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

        