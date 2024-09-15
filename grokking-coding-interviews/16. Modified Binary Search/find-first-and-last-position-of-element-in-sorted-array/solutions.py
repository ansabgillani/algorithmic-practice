class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Finds the starting and ending position of a given target value in a sorted array.
        
        Args:
            nums (List[int]): The input array of integers.
            target (int): The target value to find.
            
        Returns:
            List[int]: A list containing the first and last positions of the target. 
                      Returns [-1, -1] if the target is not found.
        """
        
        def binary_search_left(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        def binary_search_right(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        start = binary_search_left(nums, target)
        end = binary_search_right(nums, target) - 1
        
        if start < len(nums) and nums[start] == target:
            return [start, end]
        else:
            return [-1, -1]