from collections import Counter

# when going in sorted order, if we ever encouter a value whos count is non 0, it MUST be the start of a sequence
# this is gaurenteed by the sorted order and the fact that we "consume" straights as soon as we see them
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # if you can't divide it into groups, it wont work
        if len(hand) % groupSize != 0: return False
  
        card_count = Counter(hand)
        hand.sort()

        for card in hand:
            # since we're in sorted order (and we consumed previous straights), this should GUARENTEE the START of a new group
            if card_count[card]:
                # can we form a group
                for i in range(card, card + groupSize):
                    if not card_count[i]: 
                        return False
                    card_count[i] -= 1

        return True


        
                