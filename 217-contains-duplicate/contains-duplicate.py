class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for i in nums:
            if i in hashMap:
                return True
            hashMap[i] = 1
        return False