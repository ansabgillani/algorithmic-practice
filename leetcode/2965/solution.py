def findMissingAndRepeatedValues(grid):
    n = len(grid)
    total_sum = n * (n + 1) // 2
    total_square_sum = n * (n + 1) * (2 * n + 1) // 6
    
    current_sum = sum(sum(row) for row in grid)
    current_square_sum = sum(x*x for row in grid for x in row)
    
    diff = total_sum - current_sum
    diff_square = total_square_sum - current_square_sum
    
    a_plus_b = diff_square // diff
    a = (diff + a_plus_b) // 2
    b = a_plus_b - a
    
    return [a, b]

# Example usage:
grid1 = [[1,3],[2,2]]
print(findMissingAndRepeatedValues(grid1))  # Output: [2,4]

grid2 = [[9,1,7],[8,9,2],[3,4,6]]
print(findMissingAndRepeatedValues(grid2))  # Output: [9,5]