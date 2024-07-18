class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res = 0
        l,r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
#         max_left = [0]
#         max_right = [0]
        
#         for l in height:
#             max_left.append(max(l,max_left[-1]))
#         for r in height[::-1]:
#             max_right.append(max(r, max_right[-1]))
#         traps = 0
#         for i in range(len(height)):
#             water = min(max_left[i], max_right[-i-1]) - height[i]
#             if water > 0:
#                 traps += water
#         return traps
