class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # Sort both seats and students arrays
        seats.sort()
        students.sort()
        
        total_moves = 0
        
        # Calculate the total number of moves required
        for seat, student in zip(seats, students):
            total_moves += abs(seat - student)
            
        return total_moves

# Example usage:
solution = Solution()

print(solution.minMovesToSeat([3,1,5], [2,7,4]))  # Output: 4
print(solution.minMovesToSeat([4,1,5,9], [1,3,2,6]))  # Output: 7
print(solution.minMovesToSeat([2,2,6,6], [1,3,2,6]))  # Output: 4