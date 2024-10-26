class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Function to calculate the Euclidean distance from the origin
        def distance(point):
            return point[0]**2 + point[1]**2
        
        # Using a heap to find the k smallest distances efficiently
        import heapq
        closest_points = []
        
        for point in points:
            dist = distance(point)
            if len(closest_points) < k:
                heapq.heappush(closest_points, (-dist, point))
            else:
                if -dist > closest_points[0][0]:
                    heapq.heappop(closest_points)
                    heapq.heappush(closest_points, (-dist, point))
        
        # Extracting the points from the heap
        return [point for _, point in closest_points]