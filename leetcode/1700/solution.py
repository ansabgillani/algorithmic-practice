from collections import deque, Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        Returns the number of students that are unable to eat lunch.
        """
        student_queue = deque(students)
        sandwich_stack = list(sandwiches)
        
        while sandwich_stack and student_queue:
            current_sandwich = sandwich_stack[0]
            if current_sandwich in student_queue:
                student_queue.remove(current_sandwich)
                del sandwich_stack[0]
            else:
                # If no more students want the top sandwich, break
                return len(student_queue)
        
        return 0