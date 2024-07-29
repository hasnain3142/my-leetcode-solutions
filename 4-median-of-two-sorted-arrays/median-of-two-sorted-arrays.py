class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n1, n2 = len(nums1), len(nums2)
        total = n1+n2
        half = (total+1)//2
        low,high = 0, n1

        while low <= high:
            m1 = (low+high)//2
            m2 = half - m1
            l1 = nums1[m1-1] if m1-1 >= 0 else float("-infinity")
            r1 = nums1[m1] if m1 < n1 else float("infinity")
            l2 = nums2[m2-1] if m2-1 >= 0 else float("-infinity")
            r2 = nums2[m2] if m2 < n2 else float("infinity")

            if l1 <= r2 and l2 <= r1:
                if (total % 2 == 0):
                    return ((max(l1,l2) + min(r1,r2))/2 )
                return max(l1,l2)
            elif l1 > r2:
                high = m1 - 1
            else:
                low = m1 + 1