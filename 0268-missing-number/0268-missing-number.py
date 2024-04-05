class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # Calculate the sum of the elements in the array
        current_sum = sum(nums)      
        # Calculate the expected sum of a complete sequence from 0 to len(nums)
        correct_sum = len(nums) * (len(nums) + 1) // 2

        # Return the difference between the expected sum and the actual sum
        return correct_sum - current_sum


        