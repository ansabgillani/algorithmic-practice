class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # Convert numbers to strings for custom comparison
        str_nums = list(map(str, nums))
        
        # Custom comparator function
        def compare(x, y):
            return (int(y + x) - int(x + y))
        
        # Sort the array using the custom comparator
        str_nums.sort(key=functools.cmp_to_key(compare))
        
        # Edge case: if the largest number is '0', the result is '0'
        if str_nums[0] == '0':
            return '0'
        
        # Join and return the sorted array as a single string
        return ''.join(str_nums)