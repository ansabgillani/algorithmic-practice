class Solution:
    def largestNumber(self, nums):
        nums = list(map(str, nums))
        
        def compare(x, y):
            return (int(y + x) - int(x + y))
        
        nums.sort(key=functools.cmp_to_key(compare))
        
        if nums[0] == '0':
            return "0"
        
        return "".join(nums)