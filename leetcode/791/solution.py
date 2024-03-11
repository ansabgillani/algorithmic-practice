def customSortString(order: str, s: str) -> str:
    """
    Sorts string 's' according to the order specified in string 'order'.
    
    :param order: A string representing the custom order.
    :param s: The string to be sorted based on the custom order.
    :return: A new string with characters of 's' sorted according to 'order'.
    """
    # Create a dictionary to count occurrences of each character in 's'
    from collections import Counter
    char_count = Counter(s)
    
    # Build the result string based on the custom order
    result = []
    for char in order:
        if char in char_count:
            result.append(char * char_count[char])
            del char_count[char]
    
    # Append any remaining characters that are not in 'order'
    for char, count in char_count.items():
        result.append(char * count)
    
    return ''.join(result)

# Example usage
print(customSortString("cba", "abcd"))  # Output: "cbad"
print(customSortString("bcafg", "abcd"))  # Output: "bcad"