class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subset = set()
        l = 0
        r = 0
        len_of_longest_substring = 0
        while r < len(s):
            if s[r] not in subset:
                subset.add(s[r])
                len_of_longest_substring = max(len_of_longest_substring, r - l + 1)
            else:
                while s[r] in subset:
                    subset.remove(s[l])
                    l += 1
                subset.add(s[r])
                len_of_longest_substring = max(len_of_longest_substring, r - l + 1)
            r += 1
        return len_of_longest_substring