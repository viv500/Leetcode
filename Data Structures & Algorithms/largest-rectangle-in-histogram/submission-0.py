class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # time and space: O(n)
        # the stack only stores icnreaseing value heights
        # as soon as we see a height that breaks this height, keep popping stack and calculating area fromt he bar to the right
        # until we reach the one that broke increasing order (this works cuz stack is increasing)

        # the final element we pop will be the lasr height that was greater than the one the height that broke icnreasign order
        # we can extend backwardds! push a new tower onto the stac with height of the one that broke order, but index would be thre last
        # tiower that we popped cuz we're gaurenteed t be able to extend backwards till then

        # in the end, we'll have a bunch of stack elments that started at a specific index and never got popped cuz they extended
        # all the way to the end. process these by calculating width using the imaginary boundary len(heights) and seeing if we find a better area
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i # allows us to track the "last popped value" so we can extend backwards
            while stack and h < stack[-1][0]:
                height, j = stack.pop()
                width = i - j
                max_area = max(max_area, height * width)

                start = j # extending backwards
            
            # if its increasing or stack is empty, just append
            stack.append((h, start)) # dont append i, append start i.e. pushing it backwards

        # processing the final stack items that extneded all the way to the end
        while stack:
            height, index = stack.pop()
            width = len(heights) - index
            max_area =max(max_area, height * width)

        return max_area

    