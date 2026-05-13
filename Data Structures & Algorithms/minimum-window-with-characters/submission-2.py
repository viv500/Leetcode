from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # this range is ouf of boudnds, if we find nothing smaller, answer is ""
        min_string = [0, len(s) + 1]
        left, right = 0, 0
        need = Counter(t) # this is need since we have as many "need" conditions as there are unique characters 
                          # ex if its ABBC then need is 3 with B needing to be there twice as 1 "need"
        have = 0

        window = defaultdict(int)

        while right < len(s):

            while len(need) != have and right < len(s):
                # not a valid window, expand it

                window[s[right]] += 1

                if need.get(s[right], 0) == window[s[right]]: # exactly =, not > ( since we dont wanna incremet HAVE again if we find the character later)
                    have += 1
                
                right += 1

            # current window is valid!
            while len(need) == have and left <= right:
            
                if right - left < min_string[1] - min_string[0]:
                    min_string = [left, right]
            
                # shrink window
                window[s[left]] -= 1

                if s[left] in need:
                    if window[s[left]] == need[s[left]] - 1: # again, to avoid double counting
                        have -= 1
                
                left += 1
        
        return "" if min_string[1] == len(s) + 1 else s[min_string[0]: min_string[1]]

            

    