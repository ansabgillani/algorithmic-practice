class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        """
        Finds the center of a star graph given its edges.
        
        :param edges: List of lists where each sublist represents an edge in the graph.
        :return: The center node of the star graph.
        """
        # The center node will be the only node that appears in both edges
        return set(edges[0]).intersection(set(edges[1])).pop()