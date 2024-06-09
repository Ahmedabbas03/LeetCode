class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Binary Search Problem
        left = 0 
        right = len(arr)

        while left < right:
            mid = (left + right) // 2  

            if arr[mid] - (mid + 1) < k:
                left = mid + 1
            else:
                right = mid 

        return left + k
