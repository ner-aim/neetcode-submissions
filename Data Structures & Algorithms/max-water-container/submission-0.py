class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        maxVolume = -1

        while i < j:
            volume = min(heights[i], heights[j]) * (j - i)
            maxVolume = max(maxVolume, volume)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
            
        return maxVolume