class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        maxf = 0
        res = 0
        l = 0
        
        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            maxf = max(counts[s[r]], maxf)
            if (r-l + 1) - maxf > k:
                counts[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        
        return res
            