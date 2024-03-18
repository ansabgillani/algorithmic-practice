class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # Sort balloons by their end position
        points.sort(key=lambda x: x[1])
        
        # Initialize the first arrow position to the end of the first balloon
        arrow_pos = points[0][1]
        num_arrows = 1
        
        # Iterate through the sorted balloons
        for start, end in points[1:]:
            # If the current balloon starts after or when the previous arrow can still burst it
            if start > arrow_pos:
                # Move the arrow to the end of the current balloon
                arrow_pos = end
                num_arrows += 1
        
        return num_arrows