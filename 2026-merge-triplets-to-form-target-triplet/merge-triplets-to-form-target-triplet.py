class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x_exists = False
        y_exists = False
        z_exists = False

        target_x, target_y, target_z = target

        for x,y,z in triplets:
            if x > target_x or y > target_y or z > target_z:
                continue
            
            if x == target_x: x_exists = True
            if y == target_y: y_exists = True
            if z == target_z: z_exists = True

        return x_exists and y_exists and z_exists