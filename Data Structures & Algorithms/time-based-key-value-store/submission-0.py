class TimeMap:
    def __init__(self):

        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            self.hashMap[key] = []
        self.hashMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:

        result = ""
        values = self.hashMap.get(key, [])

        l = 0
        r = len(values) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if values[mid][1] <= timestamp:
                l = mid + 1
                result = values[mid][0]

            else:
                r = mid - 1

        return result
