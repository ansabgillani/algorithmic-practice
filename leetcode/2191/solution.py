class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        """
        Sorts the given array 'nums' based on their mapped values according to the provided 'mapping'.
        
        Args:
        mapping (List[int]): A list of 10 integers representing the digit mapping rule.
        nums (List[int]): The input list of integers to be sorted.
        
        Returns:
        List[int]: The sorted list of integers based on their mapped values.
        """
        def get_mapped_value(num):
            return int(''.join(str(mapping[int(digit)]) for digit in str(num)))
        
        return sorted(nums, key=get_mapped_value)