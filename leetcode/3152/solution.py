class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # Helper function to check if a subarray is special
        def is_special(subarray):
            return all((x % 2 != y % 2) for x, y in zip(subarray, subarray[1:]))

        # Process each query and check the corresponding subarray
        return [is_special(nums[l:r+1]) for l, r in queries]