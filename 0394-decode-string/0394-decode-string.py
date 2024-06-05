class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_substring = ""
        current_number = 0
        
        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
                
            elif char == '[':
                stack.append((current_substring, current_number))
                current_substring = ""
                current_number = 0
                
            elif char.isalpha():
                current_substring += char
                
            elif char == ']':
                last_substring, repeat_count = stack.pop()
                current_substring = last_substring + current_substring * repeat_count
        
        return current_substring 