class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minSoFar = float('inf')
        profit = 0
        n = len(prices)

        for i in range(1,n):
            minSoFar = min(minSoFar, prices[i-1])
            profit = max(prices[i] - minSoFar, profit)
        
        return profit