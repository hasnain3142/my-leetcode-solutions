class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        for t in tokens:
            if t.lstrip('-').isdigit():
                operands.append(int(t))
            else:
                if t == "+":
                    operands.append(operands.pop() + operands.pop())
                elif t == "-":
                    subtractor = operands.pop()
                    operands.append(operands.pop() - subtractor)
                elif t == "*":
                    operands.append(operands.pop() * operands.pop())
                elif t == "/":
                    divisor = operands.pop()
                    operands.append( int(operands.pop() / divisor))

        return operands[-1]
                    
                    