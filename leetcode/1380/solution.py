def luckyNumbers(matrix):
    """
    Find all lucky numbers in a matrix.
    
    A lucky number is defined as the minimum element in its row and 
    the maximum element in its column.
    
    :param matrix: List of lists of integers representing the matrix
    :return: List of integers representing the lucky numbers
    """
    # Get the transpose of the matrix for easier column access
    transposed = list(zip(*matrix))
    
    # Find the minimum in each row and maximum in each column
    mins_in_rows = [min(row) for row in matrix]
    maxs_in_cols = [max(col) for col in transposed]
    
    # The lucky numbers are the intersection of these two sets
    return list(set(mins_in_rows) & set(maxs_in_cols))

# Test cases
print(luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))  # Output: [15]
print(luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]))  # Output: [12]
print(luckyNumbers([[7,8],[1,2]]))  # Output: [7]