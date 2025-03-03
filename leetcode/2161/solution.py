class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        """
        Rearrange nums such that elements less than pivot appear before,
        elements equal to pivot in between, and elements greater than pivot after.
        
        Args:
        nums (List[int]): The input list of integers.
        pivot (int): The pivot value.
        
        Returns:
        List[int]: The rearranged list.
        """
        # Separate the numbers into three categories: less than pivot, equal to pivot, and greater than pivot
        less = [x for x in nums if x < pivot]
        equal = [x for x in nums if x == pivot]
        greater = [x for x in nums if x > pivot]
        
        # Combine the three lists
        return less + equal + greater