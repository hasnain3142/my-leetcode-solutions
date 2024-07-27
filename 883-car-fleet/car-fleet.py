class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        cars.sort(key=lambda x: x[0], reverse=True)

        for i in range(len(cars)):
            time = (target - cars[i][0]) / cars[i][1]
            if fleets and time <= fleets[-1]:
                continue
            fleets.append(time)
        
        return len(fleets)