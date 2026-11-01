class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        fx = fy = fz = False
        target_x, target_y, target_z = target

        for x, y, z in triplets:
            if x > target_x or y > target_y or z > target_z: continue
            if x == target_x: fx = True
            if y == target_y: fy = True
            if z == target_z: fz = True

        return fx and fy and fz