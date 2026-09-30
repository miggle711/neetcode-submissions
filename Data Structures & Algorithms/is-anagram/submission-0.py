class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 97 for 'a'
        s_ascii = [ord(char) - 97 for char in s]
        t_ascii = [ord(char) - 97 for char in t]

        s_arr = [0] * 26
        t_arr = [0] * 26

        # strings of different lengths cannot be anagrams
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            s_id = ord(s[i]) - 97
            t_id = ord(t[i]) - 97
            s_arr[s_id] += 1
            t_arr[t_id] += 1
        
        for j in range(len(s_arr)):
            if s_arr[j] != t_arr[j]:
                return False
        return True






        