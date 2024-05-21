class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Base case: return a list containing an empty subset
        if not nums:
            return [[]]
        
        # Recursive call to get all subsets of the array except the last element
        smaller_subsets = self.subsets(nums[:-1])
        
        # Add the last element to each of these subsets and append to result
        return smaller_subsets + [s + [nums[-1]] for s in smaller_subsets]