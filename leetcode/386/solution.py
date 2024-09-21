class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        """
        Return all numbers in the range [1, n] sorted in lexicographical order.
        
        Time complexity: O(n)
        Space complexity: O(1)
        """
        return map(int, sorted(map(str, range(1, n + 1))))