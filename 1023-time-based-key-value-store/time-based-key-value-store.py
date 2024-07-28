class TimeMap:

    def __init__(self):
        self.time_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_dict[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.time_dict.get(key, [])
        left = 0
        right = len(values) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)