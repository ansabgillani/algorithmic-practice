from collections import Counter

def isNStraightHand(hand, groupSize):
    """
    Check if it's possible to rearrange the cards into groups of size groupSize,
    where each group consists of consecutive cards.
    
    :type hand: List[int]
    :type groupSize: int
    :rtype: bool
    """
    if len(hand) % groupSize != 0:
        return False
    
    count = Counter(hand)
    for card in sorted(count):
        if count[card] > 0:
            for i in range(card, card + groupSize):
                count[i] -= 1
                if count[i] < 0:
                    return False
    return True

# Example usage:
print(isNStraightHand([1,2,3,6,2,3,4,7,8], 3))  # Output: true
print(isNStraightHand([1,2,3,4,5], 4))          # Output: false