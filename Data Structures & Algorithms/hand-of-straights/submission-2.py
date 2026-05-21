from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False

        hand.sort()
        counter = Counter(hand)

        for card in hand:
            if counter[card]:
                for i in range(card, card + groupSize):
                    if not counter[i]:
                        return False
                    counter[i] -= 1

        return True


