from collections import Counter

class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False

        freq = Counter(hand)
        hand.sort()
        
        for num in hand:
            if freq[num]:
                for i in range(num, num + groupSize):
                    if not freq[i]:
                        return False
                    freq[i] -= 1

        return True