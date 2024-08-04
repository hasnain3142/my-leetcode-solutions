class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []
        for i in range(len(nums)):
            numsum = 0
            for j in range(i, len(nums)):
                numsum += nums[j]
                res.append(numsum)
        res.sort()
        range_sum = 0
        mod = 10**9 + 7
        for i in range(left-1, right):
            range_sum = (range_sum + res[i]) % mod
        return range_sum