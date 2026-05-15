class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Time and space: O(n)
        #
        # Maintain a stack of bars in strictly increasing height order.
        # When we encounter a bar shorter than the stack's top, it "breaks"
        # the increasing sequence — pop and compute the area of each taller
        # bar, using the current index as the right boundary.
        #
        # Key insight — extending backwards:
        # The last bar we pop is the furthest left we could have started a
        # rectangle at the height of the bar that broke the sequence.
        # So instead of pushing the new (shorter) bar at its own index, we
        # push it at the index of the last popped bar, effectively claiming
        # all that cleared space.
        #
        # At the end, any bars still on the stack were never popped, meaning
        # they could extend all the way to the right edge. Process them using
        # len(heights) as the right boundary.

        stack = []  # stores (height, start_index)
        max_area = 0

        for i, h in enumerate(heights):
            start = i  # tracks how far left this bar can extend
            while stack and h < stack[-1][0]:
                height, j = stack.pop()
                width = i - j
                max_area = max(max_area, height * width)
                start = j  # we can now extend back to where this bar started

            stack.append((h, start))  # push with extended start, not just i

        # Any remaining bars extend to the right edge of the histogram
        while stack:
            height, index = stack.pop()
            width = len(heights) - index
            max_area = max(max_area, height * width)

        return max_area