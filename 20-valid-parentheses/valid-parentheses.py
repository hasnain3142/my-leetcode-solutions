class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeparentheses = {")" : "(",
                      "}" : "{", 
                       "]": "[" }
        
        for c in s:
            if c in closeparentheses:
                if stack and stack[-1] == closeparentheses[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False