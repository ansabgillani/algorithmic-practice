class Solution:
    def sortArray(self, arr: List[int]) -> None:
        """
        Sorts the array in-place using the mathematical formula.
        
        :param arr: List of integers from 1 to n with no duplicates.
        """
        n = len(arr)
        for i in range(n):
            # Place the correct element at its index
            while arr[i] != i + 1:
                # Swap arr[i] with the element at its correct position
                swap_idx = arr[i] - 1
                arr[i], arr[swap_idx] = arr[swap_idx], arr[i]