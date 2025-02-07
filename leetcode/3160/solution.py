class Solution:
    def findDistinctColors(self, limit, queries):
        color_dict = {}
        result = []
        
        for query in queries:
            x, y = query
            
            if x not in color_dict:
                color_dict[x] = y
            
            result.append(len(color_dict))
        
        return result