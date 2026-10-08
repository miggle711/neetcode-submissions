class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()
        clean_s = ""
        for char in s:
            if char.isalnum():
                clean_s += char
        print(clean_s)

        s = clean_s

        i = 0 
        j = len(s) - 1
        while s[i] == s[j]:
            i += 1
            j -= 1
            if i == j:
                break
        return i == j
        

        