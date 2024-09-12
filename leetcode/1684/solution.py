class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        count = 0
        
        for word in words:
            is_consistent = True
            
            for char in word:
                if char not in allowed_set:
                    is_consistent = False
                    break
                    
            if is_consistent:
                count += 1
                
        return count