class Solution:
    def sortJumbled(self, mapping, nums):
        """
        Sorts the given array 'nums' based on the mapped values of its elements.
        
        :param mapping: List[int] representing the mapping rule for digits 0-9.
        :param nums: List[int] to be sorted based on mapped values.
        :return: Sorted List[int] based on mapped values.
        """
        def getMappedValue(num):
            mapped_value = 0
            factor = 1
            while num > 0:
                digit = num % 10
                mapped_value += mapping[digit] * factor
                num //= 10
                factor *= 10
            return mapped_value
        
        return sorted(nums, key=getMappedValue)