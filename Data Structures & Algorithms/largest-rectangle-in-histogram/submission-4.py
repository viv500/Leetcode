class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] >= height:
                prev_index, prev_height = stack.pop()
                start = prev_index
                max_area = max(max_area, prev_height * (index - start))
            
            stack.append((start, height))

        # remaining bars that extend all the way
        for index, height in stack:
            max_area = max(max_area, height * (len(heights) - index))

        return max_area