from collections import defaultdict
class CountSquares:

    # y_to_x not needed -> searching in x_to_y will give us all the feasible points
    def __init__(self):
        # helps avoid key not found errors
        # accessing a non-existent key will create a key
        # lambda needed to give each x a default dict
        self.x_to_y = defaultdict(lambda: defaultdict(int))
        
    def add(self, point: List[int]) -> None:
        x, y = point
        (self.x_to_y[x])[y] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        ways = 0
        print("point", point)
        print("x to y: ", self.x_to_y)
        print("\n\n\n")

        for y_coord in self.x_to_y[x]:
            if y_coord == y: continue # this would lead to straight lines being considered squares

            side = abs(y_coord - y)
            # don't abs() the check, it loses info about the direction
            main = self.x_to_y.get(x, {})
            left = self.x_to_y.get(x - side, {})
            right = self.x_to_y.get(x + side, {})

            if y in left and y_coord in left:
                ways += (main[y_coord] * left[y] * left[y_coord])

            if y in right and y_coord in right:
                ways += (main[y_coord] * right[y] * right[y_coord])


        return ways

        
