class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}

        for word in strs:
            # Sort the characters of the word and use it as a key
            sorted_word = ''.join(sorted(word))
        
            # Append the word to the list associated with the sorted key
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
    
        # Return the values (lists of anagrams) from the dictionary
        return anagram_dict.values()