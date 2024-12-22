class Solution:
    def findBuildings(self, heights, queries):
        query_dict = {}
        for i, j in queries:
            if i < j:
                if i not in query_dict: 
                    query_dict[i] = []
                query_dict[i].append(j)
            else:
                if j not in query_dict: 
                    query_dict[j] = []
                query_dict[j].append(i)

        result = [-1] * len(queries)
        q = deque()
        
        for i, height in enumerate(sorted(heights)):
            while q and q[0] <= i:
                q.popleft()  
            
            while query_dict and len(query_dict[q[-1]]) > 0:
                j = query_dict[q[-1]].pop()
                
                if j < i:
                    result[j] = i
                    break
                    
            q.append(i)
        
        return result