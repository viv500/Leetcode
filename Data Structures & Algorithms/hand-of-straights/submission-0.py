from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # if you can't divide it into groups, it wont work
        if len(hand) % groupSize != 0: return False
        # [1, 2, 2, 3, 3, 4, 4, 5]
        group_count = 0

        card_count = Counter(hand)

        hand.sort()

        for card in hand:
            # since we're in sorted order, this GUARENTEES the START of a new group
            if card_count[card]:
                # can we form a group
                for i in range(card, card + groupSize):
                    if not card_count[i]: 
                        return False
                    card_count[i] -= 1

        return True


        
                