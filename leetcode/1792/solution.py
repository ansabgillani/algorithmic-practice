class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Function to calculate the benefit of adding one student to a class
        def benefit(passed, total):
            return (passed + 1) / (total + 1) - passed / total
        
        # Create a max heap based on the benefit of each class
        max_heap = []
        for passed, total in classes:
            heapq.heappush(max_heap, (-benefit(passed, total), passed, total))
        
        # Add extra students to the classes that maximize the increase in pass ratio
        for _ in range(extraStudents):
            _, passed, total = heapq.heappop(max_heap)
            passed += 1
            total += 1
            heapq.heappush(max_heap, (-benefit(passed, total), passed, total))
        
        # Calculate the average pass ratio after adding all extra students
        return sum(passed / total for _, passed, total in max_heap) / len(classes)