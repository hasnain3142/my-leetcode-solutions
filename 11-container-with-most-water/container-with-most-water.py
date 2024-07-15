class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            min_height =  min(height[l], height[r])
            area = (r-l) * min_height
            max_area = max(max_area, area)
            if height[l] == min_height:
                l += 1
            else:
                r -= 1
        return max_area