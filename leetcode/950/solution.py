from collections import deque
import heapq

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        """
        Reorders the deck to reveal cards in increasing order.
        
        Args:
        deck (List[int]): The initial unsorted deck of cards.
        
        Returns:
        List[int]: The ordered deck that would reveal the cards in increasing order.
        """
        # Sort the deck in descending order
        sorted_deck = deque(sorted(deck, reverse=True))
        result = deque()
        
        while sorted_deck:
            if result:
                result.appendleft(result.pop())
            result.appendleft(sorted_deck.popleft())
        
        return list(result)