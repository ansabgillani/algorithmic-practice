def makeFancyString(s):
    """
    :type s: str
    :rtype: str
    """
    # Initialize the result string and count of consecutive characters
    result = []
    count = 1
    
    # Iterate through the string starting from the second character
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            # Append at most two occurrences of the current character to the result
            result.append(s[i - 1])
            result.append(s[i - 1]) if count >= 2 else None
            count = 1
    
    # Append the last character group
    result.append(s[-1])
    result.append(s[-1]) if count >= 2 else None
    
    return ''.join(result)