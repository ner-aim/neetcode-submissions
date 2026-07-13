class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs = [[p, s] for p, s in zip(position, speed)]

        fleet = 0
        currentTime = 0

        for position, speed in sorted(pairs, reverse=True):
            destinationTime = (target - position) / speed

            if currentTime < destinationTime:
                currentTime = destinationTime
                fleet += 1

        return fleet
