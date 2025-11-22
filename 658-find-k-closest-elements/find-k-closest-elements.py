class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 2 pointers

        L = 0 
        R = len(arr) - 1

        while R - L + 1 > k:
            if abs(arr[R] - x) < abs(arr[L] - x):
                L += 1
            else:
                R -= 1

        return arr[L: R + 1]