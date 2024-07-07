class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty = numBottles
        drinks = numBottles
        numBottles = 0
        while empty >= numExchange:
            print("numBottles", numBottles)
            print("empty", empty)
            print("drinks", drinks)
            numBottles = empty // numExchange
            empty = empty % numExchange
            drinks += numBottles
            empty += numBottles
            print("numBottles", numBottles)
            print("empty", empty)
            print("drinks", drinks)
            print("loope nd")
            
        return drinks