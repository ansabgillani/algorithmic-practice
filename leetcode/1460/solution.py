class Solution:
    def canBeEqual(self, target, arr):
        # Check if both arrays have the same elements in any order
        return sorted(target) == sorted(arr)