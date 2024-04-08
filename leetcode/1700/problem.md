# Number of Students Unable to Eat Lunch

**Problem ID:** 1700  
**Difficulty:** Easy

## Content

In the school cafeteria, students queue up for lunch. Each student prefers either a circular sandwich (`0`) or a square sandwich (`1`). The sandwiches are placed in a stack, with the top sandwich on the left.

At each step:
- If the student at the front of the queue prefers the sandwich on the top of the stack, they take it and leave the queue.
- Otherwise, they leave it and go to the end of the line.

This continues until none of the students want to take the top sandwich, leaving them unable to eat.

**Function Signature:**
def countStudents(students: List[int], sandwiches: List[int]) -> int:


**Example 1:**

**Input:** students = [1,1,0,0], sandwiches = [0,1,0,1]  
**Output:** 0  
**Explanation:**  
- Front student prefers square sandwich (1) but top sandwich is circular (0), so they leave and go to the end. Queue becomes: [1,0,0,1].  
- Front student prefers square sandwich (1) but top sandwich is circular (0), so they leave and go to the end. Queue becomes: [0,0,1,1].  
- Front student prefers circular sandwich (0) and top sandwich is circular (0), so they take it and leave. Queue becomes: [0,1,1] and sandwiches become: [1,0,1].  
- Front student prefers square sandwich (1) but top sandwich is square (1), so they take it and leave. Queue becomes: [1,0] and sandwiches become: [0,1,1].  
- Front student prefers circular sandwich (0) and top sandwich is square (1), so they leave and go to the end. Queue becomes: [0,1].  
- Front student prefers circular sandwich (0) and top sandwich is square (1), so they leave and go to the end. Queue becomes: [1] and sandwiches become: [0,1].  
- Front student prefers circular sandwich (0) and top sandwich is square (1), so they take it and leave. Queue becomes: [] and sandwiches become: [].  
All students are able to eat.


**Example 2:**

**Input:** students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]  
**Output:** 3


## Constraints

- `1 <= students.length, sandwiches.length <= 100`
- `students.length == sandwiches.length`
- `sandwiches[i]` is `0` or `1`.
- `students[i]` is `0` or `1`.

## Topic Tags

Array, Stack, Queue, Simulation