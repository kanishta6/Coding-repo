class Solution:
    def canConstruct(self, a: str, b: str) -> bool:
        letter = [0 for _ in range(26)]  # Initialize an array to store letter counts (assuming lowercase English letters)

        for c in b:
            letter[ord(c) - 97] += 1  # Increment the count for each character in the magazine

        # Now, letter[] will contain counts of each character in the magazine.

        for c in a:
            letter[ord(c) - 97] -= 1  # Decrement the count for each character in the ransomNote

        # Now, letter[] will contain the difference between counts of characters in the magazine and the ransomNote.

        return not any((i < 0 for i in letter))  # Check if any count is less than 0 and return the result
