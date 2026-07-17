class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1.copy()
        j = k = 0
        for i in range(m+n):
            if j<m and k<n:
                if temp[j]<nums2[k]:
                    nums1[i] = temp[j]
                    j += 1
                else:
                    nums1[i] = nums2[k]
                    k += 1
            else:
                if j < m:
                    nums1[i] = temp[j]
                    j += 1
                if k < n:
                    nums1[i] = nums2[k]
                    k += 1