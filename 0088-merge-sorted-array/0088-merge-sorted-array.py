class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
         # Initialize a pointer for the last index of nums1
        last = m + n - 1
        
        # While there are elements in both nums1 and nums2
        while m > 0 and n > 0:
            # Compare the last elements of nums1 and nums2
            if nums1[m - 1] > nums2[n - 1]:
                # Place the larger element in nums1 at the last index
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                # Place the larger element in nums2 at the last index
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        # If there are remaining elements in nums2, copy them to nums1
        if n > 0:
            nums1[:n] = nums2[:n]