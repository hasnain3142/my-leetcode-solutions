class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        
        if h == len(piles):
            return k
        start = 1
        end = k - 1
        while start <= end:
            mid = (start + end) // 2
            hours = 0
            for p in piles:
                hours +=  math.ceil(p / mid)
                if hours > h:
                    start = mid + 1
                    break
            else:
                end = mid - 1
                k = min(k, mid)
        
        return k