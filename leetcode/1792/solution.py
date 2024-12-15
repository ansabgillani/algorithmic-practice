from heapq import heappush, heappop

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Initialize a max-heap based on the benefit of adding one more student to each class
        heap = []
        
        for pass_students, total_students in classes:
            benefit = (pass_students + 1) / (total_students + 1) - pass_students / total_students
            heappush(heap, (-benefit, pass_students, total_students))
            
        # Assign the extra students to maximize the average pass ratio
        for _ in range(extraStudents):
            _, pass_students, total_students = heappop(heap)
            new_pass_students = pass_students + 1
            new_total_students = total_students + 1
            new_benefit = (new_pass_students + 1) / (new_total_students + 1) - new_pass_students / new_total_students
            heappush(heap, (-new_benefit, new_pass_students, new_total_students))
        
        # Calculate the maximum average pass ratio
        total_ratio = sum(pass_students / total_students for _, pass_students, total_students in heap)
        return total_ratio / len(classes)

# Example usage:
solution = Solution()
print(solution.maxAverageRatio([[1,2],[3,5],[2,2]], 2))  # Output: 0.78333
print(solution.maxAverageRatio([[2,4],[3,9],[4,5],[2,10]], 4))  # Output: 0.53485