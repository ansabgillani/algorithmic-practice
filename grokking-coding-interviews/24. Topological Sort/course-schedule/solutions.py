class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Initialize graph and in-degree array
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        # Build the graph and in-degree array
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        # Initialize queue with all courses having zero in-degree
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        # Process the courses using topological sort
        visited = 0
        while queue:
            current_course = queue.popleft()
            visited += 1
            
            # Decrease the in-degree of each neighbor
            for neighbor in graph[current_course]:
                in_degree[neighbor] -= 1
                
                # If the neighbor's in-degree becomes zero, add it to the queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If all courses are visited, return True; otherwise, return False
        return visited == numCourses

# Example usage:
solution = Solution()
print(solution.canFinish(2, [[1, 0]]))  # Output: True
print(solution.canFinish(2, [[1, 0], [0, 1]]))  # Output: False