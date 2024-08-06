class Solution:
    def minimumPushes(self, word: str) -> int:
        return sum(count * (i // 8 + 1) for i, count in enumerate(sorted(Counter(word).values(), reverse=True)))
        # freq = [0] * 26
        # for i in word:
        #     freq[ord(i) - ord('a')] += 1
        # freq.sort(reverse=True)
        # multiples = [1]*8 + [2]*8 + [3]*8 + [4]*2
        # pushes = 0
        # for i in range(len(freq)):
        #     pushes += freq[i] * multiples[i]
        # return pushes