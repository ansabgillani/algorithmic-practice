from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        """
        Finds the prefix common array of two permutations A and B.
        
        :param A: List[int] - First permutation
        :param B: List[int] - Second permutation
        :return: List[int] - Prefix common array
        """
        n = len(A)
        result = [0] * n
        set_A, set_B = set(), set()
        
        for i in range(n):
            set_A.add(A[i])
            set_B.add(B[i])
            result[i] = len(set_A & set_B)
        
        return result