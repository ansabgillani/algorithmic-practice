class Solution:
    def findCenter(self, edges):
        return set(edges[0]).intersection(set(edges[1])).pop()