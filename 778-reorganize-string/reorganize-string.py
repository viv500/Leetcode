from collections import Counter
# heap solution while storing previously used character so we don't reuse
# always use the most frequently occuring character
class Solution:
    def reorganizeString(self, s: str) -> str:
        output = ""
        freq = Counter(s)
        # stored as [count, char] so that heapification is based on count
        maxHeap = [[count, char] for char,count in freq.items()]

        heapq.heapify_max(maxHeap) # O(n)
        prev = None # to start, nothing is prev

        while prev or maxHeap:
            # if impossible: if a prev character is waiting for cooldown but theres nothing else to place in between
            if prev and not maxHeap:
                return ""

            count, char = heapq.heappop_max(maxHeap)
            output += char
            count -= 1

            if prev:
                heapq.heappush_max(maxHeap, prev)
                prev = None # need to reset since its no longer prev

            if count != 0:
                prev = [count, char]

        return output

            

        