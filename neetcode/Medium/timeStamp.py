class TimeMap:

    def __init__(self):
        self.store = {} #key string value [[value,time],[val, time]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        vals = self.store.get(key, [])
        #Bin serach
        l, r = 0, len(vals) - 1
        while l<=r:
            mid = (l+r)//2
            if vals[mid][1] <= timestamp:
                res = vals[mid][0]
                l = mid+1
            else:
                r = mid-1

        return res


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)