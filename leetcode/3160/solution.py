class Solution:
    def distinctColors(self, limit: int, queries: List[List[int]]) -> List[int]:
        """
        Finds the number of distinct colors among the balls after each query.

        :param limit: The highest label of the balls.
        :param queries: A list of queries where each query is a list [x, y].
        :return: An array with the number of distinct colors after each query.
        """
        colors = set()
        result = []
        
        for x, y in queries:
            if y not in colors:
                colors.add(y)
            result.append(len(colors))
        
        return result