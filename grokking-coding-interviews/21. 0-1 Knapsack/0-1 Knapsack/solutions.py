def knapsack(W, profit, weight):
    """
    :type W: int
    :type profit: List[int]
    :type weight: List[int]
    :rtype: int
    """
    n = len(profit)
    # Create a 2D array to store the maximum value that can be achieved with each capacity and item count.
    dp = [[0 for w in range(W + 1)] for i in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weight[i - 1] <= w:
                # If current item can fit in the bag, choose the max of including or excluding it.
                dp[i][w] = max(profit[i - 1] + dp[i - 1][w - weight[i - 1]], dp[i - 1][w])
            else:
                # If current item cannot fit, take the value from the previous item.
                dp[i][w] = dp[i - 1][w]
    
    # The maximum profit is found at the bottom-right corner of the DP table.
    return dp[n][W]

# Test cases
print(knapsack(4, [1, 2, 3], [4, 5, 1]))  # Output: 3
print(knapsack(3, [1, 2, 3], [4, 5, 6]))  # Output: 0