class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        ans = [-1] * len(queries)
        stack = []
        
        for i in range(n):
            while stack and heights[stack[-1]] < heights[i]:
                j = stack.pop()
                if ans[j] == -1:
                    ans[j] = i
            stack.append(i)
            
        query_map = defaultdict(list)
        for idx, (a, b) in enumerate(queries):
            if a > b: 
                a, b = b, a
            if heights[a] < heights[b]:
                ans[idx] = b
            else:
                query_map[(a, b)].append(idx)
        
        for key, indices in query_map.items():
            a, b = key
            i = bisect_left(stack, b)
            if i < len(stack):
                ans[indices[0]] = stack[i]
        
        return ans