class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = 1 + counts.get(n,0)
        freq = [[] for i in range(len(nums)+1)]
        
        for key, val in counts.items():
            freq[val].append(key)
        res = []
        print(freq)
        for sl in range(len(freq)-1,0,-1):
            for en in freq[sl]:
                res.append(en)
                if len(res) == k:
                    return res
        
        # return sorted(hashMap, key=hashMap.get, reverse=True)[:k]
        