class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs = [(p, s) for p, s in zip(position, speed)]

        fleet = 0
        stack = []
        currentTime = 0

        for position, speed in sorted(pairs, reverse=True):
            destinationTime = (target - position) / speed

            stack.append(destinationTime)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
