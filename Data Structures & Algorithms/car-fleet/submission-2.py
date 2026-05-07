class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort by position to make the simulation easier (closer first)
        # need to measure (time of arrival)

        cars = list(zip(position, speed))
        cars.sort(reverse = True) # sort by position
        fleet = 0

        current_max = -1

        for position, speed in cars:
            arrival_time = (target - position) / speed

            if arrival_time > current_max:
                # new fleet
                # current max should be reset
                fleet += 1
                current_max = arrival_time
        return fleet
