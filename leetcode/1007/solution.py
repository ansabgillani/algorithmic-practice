class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # Check if a given number can make all elements in one row equal
        def check(x):
            rotations_top = rotations_bottom = 0
            for i in range(n):
                if tops[i] != x and bottoms[i] != x:
                    return -1
                elif tops[i] != x:
                    rotations_top += 1
                elif bottoms[i] != x:
                    rotations_bottom += 1
            return min(rotations_top, rotations_bottom)

        n = len(tops)
        # Try to make all elements equal to the first element of either top or bottom
        result = check(tops[0])
        if result != -1 or tops[0] == bottoms[0]:
            return result
        return check(bottoms[0])