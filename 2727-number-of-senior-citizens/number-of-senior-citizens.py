class Solution:
    def countSeniors(self, details: List[str]) -> int:
        old_passengers_count = 0
        for d in details:
            if int(d[11:13]) > 60:
                old_passengers_count += 1
        return old_passengers_count