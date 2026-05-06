class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        foundX = False
        foundY = False
        foundZ = False

        target_x, target_y, target_z = target

        for x, y, z in triplets:
            if x > target_x or y > target_y or z > target_z: continue

            if x == target_x: foundX = True
            if y == target_y: foundY = True
            if z == target_z: foundZ = True

        
        return foundX and foundY and foundZ