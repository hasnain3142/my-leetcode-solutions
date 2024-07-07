class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty = numBottles
        drinks = numBottles
        numBottles = 0
        while empty >= numExchange:
            numBottles = empty // numExchange
            empty = empty % numExchange
            drinks += numBottles
            empty += numBottles
            
        return drinks