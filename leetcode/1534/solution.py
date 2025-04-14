class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # Initialize the count of good triplets
        good_triplets_count = 0
        
        # Iterate over all possible triplets (i, j, k)
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, len(arr)):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            good_triplets_count += 1
        
        return good_triplets_count