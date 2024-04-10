class Solution:
    def deckRevealedIncreasing(self, deck):
        deck.sort()
        result = [0] * len(deck)
        index = 0
        step = 1

        for card in reversed(deck):
            if index == len(deck) - 1:
                result[index] = card
                break

            while step > 1:
                i = (index + step) % len(result)
                result[i], card = card, result[i]
                index = i

            result[index] = card
            index += 2
            step *= 2

        return result