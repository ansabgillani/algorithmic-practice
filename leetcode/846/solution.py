class Solution:
    def isNStraightHand(self, hand, W):
        count = {}
        
        for card in hand:
            if card in count:
                count[card] += 1
            else:
                count[card] = 1
        
        for i in sorted(hand):
            if count[i] > 0:
                for j in range(i, i+W):
                    count[j] -= 1
                    if count[j] < 0:
                        return False
        return True