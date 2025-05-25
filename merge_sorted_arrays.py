class Solution:
    def merge(self, nums1, m, nums2, n):
        try:
            if nums1 is None or nums2 is None:
                return

            # If second array is empty, do nothing
            if n == 0:
                return

            # If first array has no initial elements, copy all from nums2
            if m == 0:
                for i in range(n):
                    nums1[i] = nums2[i]
                return

            # Merge from the end to avoid overwriting elements in nums1
            i, j, k = m - 1, n - 1, m + n - 1
            while k >= 0:
                if i >= 0 and j >= 0:
                    if nums1[i] >= nums2[j]:
                        nums1[k] = nums1[i]
                        i -= 1
                    else:
                        nums1[k] = nums2[j]
                        j -= 1
                elif i < 0:
                    nums1[k] = nums2[j]
                    j -= 1
                else:
                    nums1[k] = nums1[i]
                    i -= 1
                k -= 1

        except Exception as ex:
            print(str(ex))
