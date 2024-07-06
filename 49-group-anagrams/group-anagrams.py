class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMapList = defaultdict(list)
        for word in strs:
            counts = [0] * 26
            for ch in word:
                counts[ord(ch) - ord("a")] += 1
            hashMapList[tuple(counts)].append(word)
        return hashMapList.values()
        