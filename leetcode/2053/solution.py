class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        """
        Returns the k-th distinct string in the array arr.
        If there are fewer than k distinct strings, returns an empty string.
        
        :param arr: List of strings
        :type arr: List[str]
        :param k: Integer representing the k-th position
        :type k: int
        :return: k-th distinct string or an empty string
        :rtype: str
        """
        # Count occurrences of each string
        count = {}
        for s in arr:
            if s in count:
                count[s] += 1
            else:
                count[s] = 1
        
        # Find the k-th distinct string
        for s in arr:
            if count[s] == 1 and k == 1:
                return s
            elif count[s] == 1:
                k -= 1
        
        return ""