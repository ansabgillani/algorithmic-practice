class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        def possible(dist: int) -> bool:
            ballCount = 1
            lastPosition = position[0]
            
            for i in range(1, len(position)):
                if position[i] - lastPosition >= dist:
                    ballCount += 1
                    lastPosition = position[i]
                    
                    if ballCount == m:
                        return True
        
            return False
        
        left, right = 0, max(position) - min(position)
        
        while left < right:
            mid = (left + right + 1) // 2
            if possible(mid):
                left = mid
            else:
                right = mid - 1
        
        return left