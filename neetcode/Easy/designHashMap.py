class MyHashMap:

    def __init__(self):
        self.hashMap = []

    def put(self, key: int, value: int) -> None:
        existed = False
        for i,v in enumerate(self.hashMap):
            if key == v[0]:
                 self.hashMap[i][1] = value
                 existed = True
                 break
        if not existed:
            self.hashMap.append([key,value])
            


    def get(self, key: int) -> int:
        for i, v in enumerate(self.hashMap):
            if key == v[0]:
                return v[1]
        return -1

    def remove(self, key: int) -> None:
        for i, v in enumerate(self.hashMap):
            if key == v[0]:
                self.hashMap.pop(i)
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
