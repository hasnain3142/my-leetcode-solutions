class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            middle = (low + high) // 2
            print(low, middle, high)
            if target == nums[middle]:
                return middle
            
            if target > nums[middle]:
                low = middle + 1          
            else:
                high = middle - 1
            
        return -1
        