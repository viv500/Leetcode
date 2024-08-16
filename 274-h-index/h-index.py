class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort(reverse=True)
        h_index = 0

        # to iterate through indices and list elements together
        for i, citation in enumerate(citations):
            # if there are more than i + 1 citations
            if citation >= i + 1:
                h_index = i + 1

            # the moment this condiion breaks, you wont see any more cuz of the ordering
            else:
                break

        return h_index
            

        
        
        ''' created a hashmap of every value from 0 to max(list)
        i mapped to how many papers had more than i citations
        iterated through the hashmap
        
        come on bruh... O(n^2) ???
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


        return h_index '''

