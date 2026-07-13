class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        stack = []

        for i, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                stackTemperature, stackIndex = stack.pop()
                result[stackIndex] = i - stackIndex

            stack.append([temperature, i])

        return result
