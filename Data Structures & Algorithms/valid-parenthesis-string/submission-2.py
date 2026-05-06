class Solution:
    def checkValidString(self, s: str) -> bool:
        # brute force is a decision tree with 3 options at each level -> O(3^n)
        # with caching, this can be brought down to O(n^3)

        # greedy solution: O(n)
        # keep a running count of open parenthesis (+) snd closed (-)
        # however if we only count these and stars, we lose ordering information

        # maintain a variable high and low, which track the highest and lowest diff (+/-) so far including *s
        # if at any point the high is negative, we had too many )s and cant recover from it

        # we are guarenteed that by the end of the algorithm, there was a way to form any "diff" between [low, high] by converting the stars
        # if 0 is in this range, thered a valid way to make this work

        # NOTE: need to clamp low to 0 to handle this "(*)("
        # we end up with low = 0 and high = 2 which returns True but its actually False
        # we need to discard any negative lows so we dont accidentally add to anh illegal paths
        high = 0
        low = 0
        for char in s:
            if char == "(":
                low += 1
                high += 1
            elif char == ")":
                low -= 1
                high -= 1
            # its a *, could be empty, (, or )
            else:
                low -= 1
                high += 1

            if high < 0: return False # no recovery
            low = max(0, low)

        return low <= 0 <= high

