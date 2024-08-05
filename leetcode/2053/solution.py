class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = {}
        
        for string in arr:
            if string in counts:
                counts[string] += 1
            else:
                counts[string] = 1
        
        distinct_count = 0
        for string in arr:
            if counts[string] == 1:
                distinct_count += 1
                if distinct_count == k:
                    return string
                    
        return ""