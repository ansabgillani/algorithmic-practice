def makeGood(s):
    """
    :type s: str
    :rtype: str
    """
    stack = []
    for char in s:
        if stack and abs(ord(char) - ord(stack[-1])) == 32:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

# Test cases
print(makeGood("leEeetcode"))  # Output: "leetcode"
print(makeGood("abBAcC"))      # Output: ""
print(makeGood("s"))           # Output: "s"