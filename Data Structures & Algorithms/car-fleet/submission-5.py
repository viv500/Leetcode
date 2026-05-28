class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        print(cars)
        stack = [] # push arrival times to stack

        for position, speed in cars:
            arrival_time = (target - position) / speed
            if stack and arrival_time <= stack[-1]:
                continue

            stack.append(arrival_time)

        return len(stack)