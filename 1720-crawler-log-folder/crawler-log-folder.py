class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ops = 0
        for i in logs:
            if i == "./":
                continue
            if i == "../":
                ops = 0 if ops == 0 else ops - 1
            else:
                ops += 1
        return ops