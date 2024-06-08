class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Create hashset
        # Check if number in hashset, if it is then we already since them and we can return true
        # else add to the hashset
        # return false 
        
        
        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
                
        return False
        