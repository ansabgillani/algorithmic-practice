import heapq

class Solution:
    def minCostToConnectRopes(self, ropes: List[int]) -> int:
        """
        Connect n ropes into one rope with the minimum possible cost.
        
        :param ropes: List of integers representing the lengths of ropes.
        :return: Integer representing the minimum cost to connect all ropes.
        """
        if not ropes or len(ropes) == 1:
            return 0
        
        # Initialize a min heap
        heapq.heapify(ropes)
        
        total_cost = 0
        
        # Continue until only one rope is left
        while len(ropes) > 1:
            # Extract the two smallest ropes
            first_min = heapq.heappop(ropes)
            second_min = heapq.heappop(ropes)
            
            # Calculate the cost to connect them
            current_cost = first_min + second_min
            
            # Add the cost to the total
            total_cost += current_cost
            
            # Push the new rope back into the heap
            heapq.heappush(ropes, current_cost)
        
        return total_cost

# Test cases
solution = Solution()

print(solution.minCostToConnectRopes([8, 4, 6, 12]))  # Output: 58
print(solution.minCostToConnectRopes([20, 4, 8, 2]))   # Output: 54
print(solution.minCostToConnectRopes([1, 2, 5, 10, 35, 89]))  # Output: 224
print(solution.minCostToConnectRopes([2, 2, 3, 3]))  # Output: 20