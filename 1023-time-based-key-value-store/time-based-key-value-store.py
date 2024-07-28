class TimeMap:

    def __init__(self):
        self.time_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_dict[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        values = self.time_dict.get(key, "")
        left = 0
        right = len(values) - 1
        closest_timestamp = 0
        closest_index = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            if values[mid][0] < timestamp:
                if values[mid][0] > closest_timestamp:
                    closest_timestamp = values[mid][0]
                    closest_index = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return "" if not values or not closest_timestamp else values[closest_index][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)