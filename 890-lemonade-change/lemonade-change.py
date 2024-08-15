class Solution:
    #greedy: give the highest dennominations out first 
    # make the register a dictionary not an array for more efficient read writes and searches
    # no need to track 20s cuz you cant provide change
    def lemonadeChange(self, bills: List[int]) -> bool:
        register = {5: 0, 10: 0}

        for i in bills:
            if i == 5:
                register[i] += 1
            elif i == 10:
                if register[5] < 1:
                    return False
                else:
                    register[10] += 1

                    register[5] -= 1
            else:
                # edge case: larger denominations change when possible
                if register[5] >= 1 and register[10] >= 1:

                    register[5] -= 1
                    register[10] -= 1
                elif register[5] >= 3:
                    
                    register[5] -= 3
                else:
                    return False
        
        return True