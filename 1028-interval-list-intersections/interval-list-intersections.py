class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []

        p1 = p2 = 0
        output = []
        while p1 < len(firstList) and p2 < len(secondList):
            first, second = firstList[p1], secondList[p2]
            start = max(first[0], second[0])
            end = min(first[1], second[1])

            if start <= end:
                output.append([start, end])

            if first[1] > second[1]:
                p2 += 1
            else:
                p1 += 1

        return output
