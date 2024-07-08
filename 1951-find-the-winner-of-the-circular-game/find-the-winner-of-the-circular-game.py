class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i for i in range(1,n+1)]
        start = 0
        for i in range(n-1):
            start = (start - 1) + k
            start = start % n if start >= n else start
            print(start, friends)
            del friends[start]
            n -= 1
        return friends[0]
            
        