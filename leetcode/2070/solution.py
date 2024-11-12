class Solution:
    def maximumBeauty(self, items, queries):
        # Sort items based on price
        items.sort()
        
        # Update beauty to be the maximum beauty seen so far
        max_beauty_so_far = 0
        for i in range(len(items)):
            max_beauty_so_far = max(max_beauty_so_far, items[i][1])
            items[i][1] = max_beauty_so_far
        
        result = []
        for query in queries:
            # Use binary search to find the maximum beauty for each query
            left, right = 0, len(items) - 1
            best_beauty = 0
            while left <= right:
                mid = (left + right) // 2
                if items[mid][0] > query:
                    right = mid - 1
                else:
                    best_beauty = max(best_beauty, items[mid][1])
                    left = mid + 1
            result.append(best_beauty)
        
        return result