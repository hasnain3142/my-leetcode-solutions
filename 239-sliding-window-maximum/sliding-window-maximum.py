class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = collections.deque()
        outputs = []
        
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d += i,
            if d[0] == i-k:
                d.popleft()
            if i-k >= -1:
                outputs.append(nums[d[0]])
        return outputs
        
        
#         maxNums = []
#         l = 0
#         windowMax = max(nums[:k])
#         maxNums.append(windowMax)
        
#         for r in range(k,len(nums)):
#             if nums[l] == windowMax:
#                 windowMax = max(nums[l+1:r+1])
#             else:
#                 windowMax = nums[r] if nums[r] > windowMax else windowMax
#             maxNums.append(windowMax)
#             l += 1
#         print(maxNums)
#         return maxNums
                
        