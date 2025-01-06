from collections import defaultdict

def totalFruit(fruits):
    """
    :type fruits: List[int]
    :rtype: int
    """
    # Dictionary to store the count of each type of fruit in the current window
    basket = defaultdict(int)
    left = 0
    max_fruits = 0
    
    for right in range(len(fruits)):
        basket[fruits[right]] += 1
        
        # If we have more than two types of fruits, shrink the window from the left
        while len(basket) > 2:
            basket[fruits[left]] -= 1
            if basket[fruits[left]] == 0:
                del basket[fruits[left]]
            left += 1
        
        # Update the maximum number of fruits collected
        max_fruits = max(max_fruits, right - left + 1)
    
    return max_fruits

# Example usage:
# print(totalFruit([1,2,1]))  # Output: 3
# print(totalFruit([0,1,2,2]))  # Output: 3
# print(totalFruit([1,2,3,2,2]))  # Output: 4