class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # 2 pointer approach
        # sorting helps form contiguous blocks of common prefix words O(n log n)
        products.sort()

        L, R = 0, len(products) - 1
        result = []

        for i in range(len(searchWord)):
            word = searchWord[i]
            while L <= R and (len(products[L]) <= i or products[L][i] != word):
                L += 1

            while L <= R and (len(products[R]) <= i or products[R][i] != word):
                R -= 1

            result.append(products[L:R + 1][:3])

        return result
            

        