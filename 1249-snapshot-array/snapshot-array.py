from collections import defaultdict
from bisect import bisect_right
class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.snap_info = []

        # first value in this array represents the "live value"
        self.history = [[[0, 0]] for _ in range(length)]


    def set(self, index: int, val: int) -> None:
        h = self.history[index]
        snap_id = self.snap_id
        # no snaps happened, can just set
        if h[-1][0] == snap_id:
            h[-1][1] = val
        else:
            h.append([snap_id, val])


        
    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
        

    def get(self, index: int, snap_id: int) -> int:
        h = self.history[index]
        i = bisect_right(h, [snap_id, float("inf")]) - 1
        return h[i][1]
        
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)