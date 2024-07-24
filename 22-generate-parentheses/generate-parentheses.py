class Solution:
    def generateParenthesis(self, n: int) -> List[str]: 
        openN, closeN = 0,0
        stack, res = [], []
        
        def generate_parenthesis(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                generate_parenthesis(openN+1, closeN)
                stack.pop()
                
            
            if closeN < openN:
                stack.append(")")
                generate_parenthesis(openN, closeN+1)
                stack.pop()
            
        
        generate_parenthesis(0,0)
        return res
            
