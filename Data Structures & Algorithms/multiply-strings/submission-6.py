class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # expected solution doesn't involve any large numbers, so use result array

        # largest possible product
        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                # need to calculate offset for each (i, j) pair
                # distance from the right
                offset = (len(num2) - i - 1) + (len(num1) - j - 1)

                # index of result
                index = len(result) - offset - 1

                result[index] += (int(num1[i]) * int(num2[j]))

                # handling double digit numbers
                if result[index] >= 10:
                    first, second = result[index] // 10, result[index] % 10 

                    result[index] = second
                    result[index - 1] += first

            offset -= 1

        # map(str, result) converts [1, 2, 3] to ["1", "2", "3"]

        return "".join(map(str, result)).lstrip("0") or "0" # this handles the case where everything is 0