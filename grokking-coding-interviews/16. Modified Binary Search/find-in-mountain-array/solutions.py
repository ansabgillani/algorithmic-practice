class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # Step 1: Find the peak of the mountain array
        left, right = 0, mountainArr.length() - 1
        while left < right:
            mid = (left + right) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        
        peak = left
        
        # Step 2: Search in the increasing part of the array
        left, right = 0, peak
        while left <= right:
            mid = (left + right) // 2
            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # Step 3: Search in the decreasing part of the array
        left, right = peak, mountainArr.length() - 1
        while left <= right:
            mid = (left + right) // 2
            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) < target:
                right = mid - 1
            else:
                left = mid + 1
        
        # Step 4: Target not found
        return -1