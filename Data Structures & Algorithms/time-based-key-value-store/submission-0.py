class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.hashmap:
            self.hashmap[key] = {}

        self.hashmap[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.hashmap:
            return ""

        # exact timestamp exists
        if timestamp in self.hashmap[key]:
            return self.hashmap[key][timestamp]

        # find greatest timestamp <= given timestamp
        max_time = -1

        for t in self.hashmap[key]:

            if t <= timestamp:
                max_time = max(max_time, t)

        if max_time == -1:
            return ""

        return self.hashmap[key][max_time]