class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        
        if n > m:
            return ""
        
        tcount, window = {}, {}
        
        for i in t:
            tcount[i] = 1 + tcount.get(i, 0)
            
        have, need = 0, len(tcount)
        res, reslen = [-1,-1], m+2
        l = 0
        
        for r in range(len(s)):
            print(reslen)
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            if c in tcount and tcount[c] == window[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < reslen:
                    reslen = r - l + 1
                    res = [l, r]
                d = s[l]
                window[d] -= 1
                if d in tcount and window[d] < tcount[d]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if reslen != m+2 else ""
                