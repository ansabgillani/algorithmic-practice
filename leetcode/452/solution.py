class Solution:
    def findMinArrowShots(self, points):
        if not points:
            return 0
        
        # Sort balloons by their end position
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        current_end = points[0][1]
        
        for start, end in points[1:]:
            if start > current_end:
                arrows += 1
                current_end = end
        
        return arrows