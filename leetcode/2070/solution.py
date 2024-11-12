class Solution:
    def mostBeautifulItemForEachQuery(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Sort items by price and keep track of the max beauty encountered so far
        sorted_items = sorted(items)
        max_beauty_so_far = 0
        
        # Create a list to store the maximum beauty for each price
        price_to_max_beauty = {}
        for price, beauty in sorted_items:
            max_beauty_so_far = max(max_beauty_so_far, beauty)
            price_to_max_beauty[price] = max_beauty_so_far
        
        # Process queries and find the maximum beauty for each query
        result = []
        for query in queries:
            if query not in price_to_max_beauty:
                # Find the largest price less than or equal to the query using binary search
                idx = bisect.bisect_right(sorted_items, [query + 1, float('inf')])
                if idx > 0:
                    result.append(sorted_items[idx - 1][1])
                else:
                    result.append(0)
            else:
                result.append(price_to_max_beauty[query])
        
        return result