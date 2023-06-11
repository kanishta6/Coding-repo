class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest_palindrome = ''
        dp = [[False] * n for _ in range(n)]

        # All substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True
            longest_palindrome = s[i]

        max_length = 1

        # Check for substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                longest_palindrome = s[i:i + 2]
                max_length = 2

        # Check for substrings of length greater than 2
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if length > max_length:
                        longest_palindrome = s[i:j + 1]
                        max_length = length

        return longest_palindrome
