class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=''
        for i in s.lower():
            if i.isalpha() or i.isnumeric():
                string+=i
        if string == string[::-1]:
            return True
        return False