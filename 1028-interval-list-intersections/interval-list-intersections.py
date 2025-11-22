class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        p1 = p2 = 0
        output = []
        while p1 < len(firstList) and p2 < len(secondList):
            first = firstList[p1]
            second = secondList[p2]

            start = max(first[0], second[0])
            end = min(first[1], second[1])

            if end >= start:
                output.append([start, end])

            if first[1] > second[1]:
                p2 += 1
            else:
                p1 += 1
        return output