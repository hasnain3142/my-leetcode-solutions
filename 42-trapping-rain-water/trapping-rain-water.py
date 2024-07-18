class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0]
        max_right = [0]
        
        for l in height:
            max_left.append(max(l,max_left[-1]))
        for r in height[::-1]:
            max_right.append(max(r, max_right[-1]))
        traps = 0
        for i in range(len(height)):
            water = min(max_left[i], max_right[-i-1]) - height[i]
            if water > 0:
                traps += water
        return traps
