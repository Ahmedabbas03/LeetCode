class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""
        
        s = s.lower()
        
        for char in s:
            if char.isalnum():
                new_string += char
            
        return new_string == new_string[::-1]