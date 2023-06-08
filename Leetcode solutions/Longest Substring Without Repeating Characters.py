class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = {}
        l=0
        length = 0

        for r in range(len(s)):
            char = s[r]
            if char in charset and charset[char]>=l :
                l = charset[char] + 1
            else:
                length = max(length,r-l+1)
            charset[char]=r

        return length  