from collections import defaultdict
class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        # IMPORTANT: can't use a set (optimal) cuz it doesnt track count
        # if you remove element from the set when shrinking window, you don't really know if theres more occurances in current window
        # ex. [3,3,3,1,2,1,1,2,3,3,4]
        # condition is met when you set.remove(3) so shrinking stops. but 3 is still in thee window!!

        if len(set(fruits)) == 1 or len(set(fruits)) == 2: # only 1 or 2 fruit types
            return len(fruits)
    
        
        L = R = 0
        longest = 0
        baskets = defaultdict(int) # cleaner code, initializes all values as 0

        while(R < len(fruits)):
            baskets[fruits[R]] += 1

            while(len(baskets) > 2):
                baskets[fruits[L]] -= 1

                if baskets[fruits[L]] == 0:
                    baskets.pop(fruits[L]) # IMPORTANT: deleting a key from dictionary so length stays the same
                    
                L += 1

            longest = max(longest, R - L + 1)

            R += 1

        return longest
