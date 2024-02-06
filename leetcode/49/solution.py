class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups anagrams together from a list of strings.
        
        :param strs: List of strings to be grouped
        :return: List of lists where each sublist contains anagrams
        """
        # Dictionary to store sorted string as key and list of anagrams as value
        anagram_dict = {}
        
        for s in strs:
            # Sort the characters of the string and use it as a key
            sorted_str = ''.join(sorted(s))
            
            if sorted_str not in anagram_dict:
                anagram_dict[sorted_str] = []
            
            anagram_dict[sorted_str].append(s)
        
        return list(anagram_dict.values())