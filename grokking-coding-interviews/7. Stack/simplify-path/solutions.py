def simplifyPath(path: str) -> str:
    """
    Simplify a given Unix-style absolute path.
    
    Parameters:
    path (str): The original path to be simplified.
    
    Returns:
    str: The simplified canonical path.
    """
    stack = []
    components = path.split('/')
    
    for component in components:
        if component == '' or component == '.':
            continue
        elif component == '..':
            if stack:
                stack.pop()
        else:
            stack.append(component)
    
    return '/' + '/'.join(stack)

# Example usage:
simplified_path = simplifyPath("/home//foo/")
print(simplified_path)  # Output: "/home/foo"