class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            rate_per_h = (left + right) // 2
            hours = sum(math.ceil(p / rate_per_h) for p in piles)

            if hours <= h:
                res = rate_per_h
                right = rate_per_h - 1
            else:
                left = rate_per_h + 1

        return res