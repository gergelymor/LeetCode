#146. LRU Cache

import time

class LRUCache:
    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = dict()
        self.usage = dict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.usage[key] = time.time()
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.usage[key] = time.time()
        else: 
            if len(self.cache) < self.size:
                self.cache[key] = value
                self.usage[key] = time.time()
            else:
                leastUsedKey = min(self.usage, key=self.usage.get)
                del self.usage[leastUsedKey]
                del self.cache[leastUsedKey]
                self.cache[key] = value
                self.usage[key] = time.time()
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
