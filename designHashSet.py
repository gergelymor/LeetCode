#705. Design HashSet

class MyHashSet:

    def __init__(self):
        self.container = list()
        
    def add(self, key: int) -> None:
        if not self.contains(key):
            self.container.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            obj = list()
            for i in range(0, len(self.container)):
                if self.container[i] != key:
                    obj.append(self.container[i])
            self.container = obj

    def contains(self, key: int) -> bool:
        for i in range(0, len(self.container)):
            if self.container[i] == key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
