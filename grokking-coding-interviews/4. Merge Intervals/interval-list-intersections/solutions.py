class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        Finds the intersection of two lists of closed intervals.

        Parameters:
        firstList (List[List[int]]): The first list of intervals.
        secondList (List[List[int]]): The second list of intervals.

        Returns:
        List[List[int]]: A list of intersecting intervals.
        """
        i, j = 0, 0
        result = []

        while i < len(firstList) and j < len(secondList):
            # Calculate the intersection of firstList[i] and secondList[j]
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            if start <= end:
                result.append([start, end])

            # Move to the next interval that ends earlier
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return result

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))  # Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    print(solution.intervalIntersection([[1,3],[5,9]], []))  # Output: []