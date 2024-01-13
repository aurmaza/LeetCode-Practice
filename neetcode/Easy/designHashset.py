class MyHashSet:

    def __init__(self):
        self.hashset = []

    def add(self, key: int) -> None:
        if key not in self.hashset:
            self.hashset.append(key)
        

    def remove(self, key: int) -> None:
        for i,v in enumerate(self.hashset):
            if v == key:
                self.hashset.pop(i)


    def contains(self, key: int) -> bool:
        for n in self.hashset:
            if key == n:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
