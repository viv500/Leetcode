class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        remove_close = []
        running = 0

        for c in s:
            if c == "(": running += 1
            elif c == ")": running -= 1

            if running == -1:
                running = 0
                continue

            remove_close.append(c)

        running = 0

        result = []
        for i in range(len(remove_close) -1, -1, -1):
            c = remove_close[i]
            if c == "(": running += 1
            elif c == ")": running -= 1

            if running == 1:
                running = 0
                continue

            result.append(c)


        return "".join(result[::-1])