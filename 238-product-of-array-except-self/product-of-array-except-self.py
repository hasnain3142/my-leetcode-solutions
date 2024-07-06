class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr_size = len(nums)
        answer = [0]*arr_size
        prefix = 1
        for i in range(arr_size):
            answer[i] = prefix
            prefix = prefix * nums[i]
        postfix = 1
        for i in range(arr_size-1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
        return answer