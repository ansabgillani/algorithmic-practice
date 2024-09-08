def subsetsWithDup(nums):
    """
    Generate all possible subsets of a given list of integers, including duplicates.
    
    :param nums: List[int] - A list of integers that may contain duplicates.
    :return: List[List[int]] - A list of lists representing all possible subsets without duplicates.
    """
    from itertools import combinations
    
    # Initialize a set to store unique subsets
    result = set()
    
    # Iterate over all possible lengths of subsets
    for r in range(len(nums) + 1):
        # Generate all combinations of length r and add them to the set
        for combo in combinations(sorted(nums), r):
            result.add(combo)
    
    # Convert the set back to a list and return
    return [list(subset) for subset in result]

# Example usage:
if __name__ == "__main__":
    nums1 = [1, 2, 2]
    print(subsetsWithDup(nums1))  # Output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

    nums2 = [0]
    print(subsetsWithDup(nums2))  # Output: [[], [0]]