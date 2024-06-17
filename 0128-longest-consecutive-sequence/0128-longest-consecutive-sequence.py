class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        longest_length = 0
        
        for num in nums:
            if num - 1 not in nums:
                current_length = 1
                current_num = num
                
                while current_num + 1 in nums:
                    current_num += 1
                    current_length += 1
                   
                longest_length = max(longest_length, current_length)
                
        return longest_length
    
# Time: O(n)
# Space: O(n)