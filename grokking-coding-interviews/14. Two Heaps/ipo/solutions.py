import heapq

def findMaximizedCapital(k, w, profits, capital):
    """
    :type k: int
    :type w: int
    :type profits: List[int]
    :type capital: List[int]
    :rtype: int
    """
    n = len(profits)
    projects = list(zip(capital, profits))
    projects.sort()  # Sort projects by capital required
    
    max_heap = []
    i = 0
    
    for _ in range(k):
        while i < n and projects[i][0] <= w:
            heapq.heappush(max_heap, -projects[i][1])  # Use negative to simulate a max heap
            i += 1
        
        if not max_heap:
            break
        
        w -= heapq.heappop(max_heap)
    
    return w

# Example usage:
# k = 2
# w = 0
# profits = [1, 2, 3]
# capital = [0, 1, 1]
# print(findMaximizedCapital(k, w, profits, capital))  # Output: 4