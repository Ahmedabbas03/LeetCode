class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char = set()
        result = 0
        left = 0
        
        for right in range(len(s)):
            while s[right] in char:
                char.remove(s[left])
                left += 1
                
            char.add(s[right])
            result = max(result, right - left + 1)
            
        return result
            
    # Time:  O(n)
    # Space: O(n)
        