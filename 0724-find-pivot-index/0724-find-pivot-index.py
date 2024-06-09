class Solution:
    def pivotIndex(self, nums: List[int]) -> int:


         #  0,1,2,3,4,5
         # [1,7,3,6,5,6]
         #        ^
         # [1,7,3] = 11 = [5,6] = 11


        total = sum(nums)
        leftSum  = 0

        for index in range(len(nums)):
            rightSum = total - nums[index] - leftSum
            if leftSum == rightSum:
                return index 
            leftSum += nums[index] 

        return -1


