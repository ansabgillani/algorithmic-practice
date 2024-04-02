class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_t = {}
        t_chars = set()
        
        for char_s, char_t in zip(s, t):
            if char_s in map_s_t and map_s_t[char_s] != char_t:
                return False
            if char_s not in map_s_t and char_t in t_chars:
                return False
            map_s_t[char_s] = char_t
            t_chars.add(char_t)
        
        return True