class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # 2 pointer approach
        # sorting helps form contiguous blocks of common prefix words O(n log n)
        # Time = O(nlogn + m + n) where n = size of products, m = size of searchword
        products.sort()

        L, R = 0, len(products) - 1
        result = []

        for i in range(len(searchWord)):
            word = searchWord[i]
             # need to check L doesnt cross R and
             # if either theres a character mismatch or the word is too short, skip
            while L <= R and (len(products[L]) <= i or products[L][i] != word):
                L += 1

            while L <= R and (len(products[R]) <= i or products[R][i] != word):
                R -= 1

            result.append(products[L:R + 1][:3])

        return result
            

        