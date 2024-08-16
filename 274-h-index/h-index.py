class Solution:
    def hIndex(self, citations: List[int]) -> int:

        if not citations:
            return 0

        has = {}
        highest = max(citations)

        for i in range(highest + 1):
            has[i] = 0

        for i in has:
            for j in citations:
                if j >= i:
                    has[i] += 1

        h_index = 0

        for i in has:
            if i <= has[i] and i > h_index:
                h_index = i


        return h_index

