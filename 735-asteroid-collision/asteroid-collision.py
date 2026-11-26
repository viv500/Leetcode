# note: collision needs + -, cant be - +
# idea: should stack win? set a = 0. should current win? stack.pop()
# should neither win? do both
class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                diff = stack[-1] + a

                if diff < 0:
                    stack.pop() # remove the smaller negative
                elif diff > 0:
                    a = 0 # null it out so it doesnt get added
                else:
                    stack.pop() # we dont want neither
                    a = 0

            if a != 0: stack.append(a)

        return stack