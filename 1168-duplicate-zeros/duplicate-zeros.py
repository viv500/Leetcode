class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        counter = 0
        length = len(arr)

        while counter < length:
            if arr[counter] == 0 and counter != length - 1:
                for i in range(length - 1, counter, -1):
                    arr[i] = arr[i - 1]

                arr[counter + 1] = 0
                counter += 2
            else:
                counter += 1

        