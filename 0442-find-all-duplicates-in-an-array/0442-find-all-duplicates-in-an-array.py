class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ## APPROACH : INDEX AS HASHKEY ##
        ## 1. we place and swap all elements to their respective index, if we already have number in there, note it ##
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(1) ##

        duplicates = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                duplicates.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1

        return duplicates