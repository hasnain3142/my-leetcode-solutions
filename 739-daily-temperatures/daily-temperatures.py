class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        outputs = [0]*len(temperatures)
        for i, n in enumerate(temperatures):
            while stack and n > temperatures[stack[-1]]:
                ind = stack.pop()
                outputs[ind] = i-ind
            stack.append(i)
            
        return outputs
            