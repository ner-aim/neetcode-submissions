class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def sumHelper(speed):
            pilesSum = [math.ceil(x / speed) for x in piles]

            return sum(pilesSum)

        l = 1
        r = max(piles)
        result = r

        while l <= r:
            mid = l + (r - l) // 2
            if sumHelper(mid) <= h:
                r = mid - 1
                result = mid
            else:
                l = mid + 1

        return result
