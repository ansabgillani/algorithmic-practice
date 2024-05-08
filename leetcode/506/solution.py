def findRelativeRanks(score):
    """
    :type score: List[int]
    :rtype: List[str]
    """
    # Create a list of tuples (score, original index)
    indexed_scores = [(score[i], i) for i in range(len(score))]
    
    # Sort the scores in descending order
    sorted_scores = sorted(indexed_scores, reverse=True)
    
    # Initialize the result array with empty strings
    ranks = [""] * len(score)
    
    # Assign ranks based on the sorted positions
    for rank, (_, idx) in enumerate(sorted_scores):
        if rank == 0:
            ranks[idx] = "Gold Medal"
        elif rank == 1:
            ranks[idx] = "Silver Medal"
        elif rank == 2:
            ranks[idx] = "Bronze Medal"
        else:
            ranks[idx] = str(rank + 1)
    
    return ranks

# Example usage:
# print(findRelativeRanks([5,4,3,2,1]))  # Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
# print(findRelativeRanks([10,3,8,9,4])) # Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]