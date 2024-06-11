class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Create a dictionary to store the index of each element in arr2
        order = {x: i for i, x in enumerate(arr2)}
        
        # Sort arr1 using a custom key
        return sorted(arr1, key=lambda x: (order.get(x, float('inf')), x))