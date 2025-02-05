class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # If the strings are already equal, no swap is needed
        if s1 == s2:
            return True
        
        # Initialize lists to store indices where characters differ
        diff_indices = []
        
        # Iterate through the strings and collect differing indices
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_indices.append(i)
            
            # If more than 2 differences are found, return False
            if len(diff_indices) > 2:
                return False
        
        # If there are no differences, strings are already equal
        if not diff_indices:
            return True
        
        # Check if swapping the differing characters makes the strings equal
        i, j = diff_indices
        return s1[i] == s2[j] and s1[j] == s2[i]