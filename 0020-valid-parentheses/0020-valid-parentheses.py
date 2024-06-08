class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        brackets = {'(': ')', '{': '}', '[': ']'}
        
        for bracket in s:
            if bracket in brackets:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if brackets[top] != bracket:
                    return False
                
        return not stack
    

