class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""

        for char in s:
            if char.isalnum():
                new += char.lower()

        left = 0
        right = len(new) - 1

        while left < right:
            if new[left] != new[right]:
                return False
            else:
                left += 1
                right -= 1

        return True