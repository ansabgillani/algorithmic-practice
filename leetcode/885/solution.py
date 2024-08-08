def spiralMatrixIII(R, C, r0, c0):
    """
    :type R: int
    :type C: int
    :type r0: int
    :type c0: int
    :rtype: List[List[int]]
    """
    result = []
    x, y = r0, c0
    dx, dy = 0, 1  # Start moving east
    steps = 0

    while len(result) < R * C:
        if 0 <= x < R and 0 <= y < C:
            result.append([x, y])
        
        steps += 1
        if steps % 2 == 0:  # Change direction every two steps
            dx, dy = dy, -dx
        
        x, y = x + dx, y + dy

    return result