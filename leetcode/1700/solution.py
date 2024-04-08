class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Iterate over each type of sandwich in the stack.
        for s in sandwiches:
            if s not in students: 
                return len(students)
            students.remove(s)
        return 0