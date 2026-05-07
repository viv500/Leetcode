class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort by position to make the simulation easier (closer first)
        # need to measure (time of arrival)
        # all we care about is time of arrival in sorted order of position
        # stack could work but tracking fleet leaders arrival time is better

        cars = list(zip(position, speed))
        cars.sort(reverse = True) # sort by position
        fleet = 0

        fleet_leader_arrival_time = -1

        for position, speed in cars:
            arrival_time = (target - position) / speed

            if arrival_time > fleet_leader_arrival_time:
                # new fleet
                # current max should be reset
                fleet += 1
                fleet_leader_arrival_time = arrival_time

        return fleet

        # stack solution:
        # only append fleet leaders to stack. if its not a fleet leader, skip
        stack = []
        for position, speed in cars:
            arrival_time = (target - position) / speed
            if not stack or arrival_time > stack[-1]:
                stack.append(arrival_time)
        return len(stack)
