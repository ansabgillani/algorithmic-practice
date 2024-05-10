class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        heap = []
        n = len(arr)
        
        for j in range(1, n):
            heappush(heap, (arr[0] / arr[j], 0, j))
        
        while k:
            frac, i, j = heappop(heap)
            if i + 1 < j:
                heappush(heap, (arr[i+1] / arr[j], i+1, j))
            k -= 1
        
        return [arr[i], arr[j]]