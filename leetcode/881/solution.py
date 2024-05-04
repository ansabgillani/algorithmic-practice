class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        # Sort the list of people by weight
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0
        
        while left <= right:
            if people[left] + people[right] <= limit:
                # If the lightest and heaviest can share a boat
                left += 1
            # Always move the pointer for the heaviest person
            right -= 1
            boats += 1
        
        return boats

# Example usage:
# solution = Solution()
# print(solution.numRescueBoats([1,2], 3))  # Output: 1
# print(solution.numRescueBoats([3,2,2,1], 3))  # Output: 3
# print(solution.numRescueBoats([3,5,3,4], 5))  # Output: 4