from collections import defaultdict, deque

def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    # Create adjacency list and in-degree array
    adj_list = defaultdict(list)
    in_degree = [0] * numCourses
    
    for course, prereq in prerequisites:
        adj_list[prereq].append(course)
        in_degree[course] += 1
    
    # Initialize queue with courses having zero in-degree
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    result = []
    
    while queue:
        current_course = queue.popleft()
        result.append(current_course)
        
        for neighbor in adj_list[current_course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If the length of the result is equal to numCourses, return it; otherwise, return an empty array
    return result if len(result) == numCourses else []

# Example usage
print(findOrder(2, [[1, 0]]))  # Output: [0, 1]
print(findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))  # Output: [0, 2, 1, 3] or any valid order
print(findOrder(1, []))  # Output: [0]