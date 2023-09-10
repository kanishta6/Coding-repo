import re

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(re.sub(r'\s{1,}', ' ', s.strip()).split(' ')[::-1])
        