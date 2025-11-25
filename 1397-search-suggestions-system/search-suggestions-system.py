class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        output = []
        L, R = 0, len(products) - 1

        for i in range(len(searchWord)):
            char = searchWord[i]

            while L <= R and (len(products[L]) <= i or products[L][i] != char):
                L += 1

            while L <= R and (len(products[R]) <= i or products[R][i] != char):
                R -= 1

            output.append(products[L:R+1][:3])

        return output


