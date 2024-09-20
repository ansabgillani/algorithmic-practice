class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """
        Finds the smallest character in 'letters' that is lexicographically greater than 'target'.
        If no such character exists, returns the first character in 'letters'.
        :param letters: List of sorted characters
        :param target: Target character to compare against
        :return: Smallest character greater than target or first character if not found
        """
        left, right = 0, len(letters) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return letters[left % len(letters)]