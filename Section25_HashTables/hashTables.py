class HashTable:
    def __init__(self, size = 2):
        self.keyMap = [None] * size
        
    def _hash(self, key):
        total = 0
        WEIRD_PRIME = 31
        for i in range(min(len(key), 100)):
            char = key[i]
            value = ord(char) - 96
            total = (total * WEIRD_PRIME + value) % len(self.keyMap)
        return total
    
    def set(self, key, value):
        index = self._hash(key)
        element = self.keyMap[index]
        if element is None:
            self.keyMap[index] = []
        self.keyMap[index].append({ key : value })
            
    def get(self, key):
        index = self._hash(key)
        element = self.keyMap[index]
        if element is not None:
            for eachElement in element:
                if key in eachElement:
                    return eachElement[key]
        return None
                    
    def keys(self):
        keySet = set()
        for element in self.keyMap:
            if element is None: continue     
            for eachElement in element:
                keys = eachElement.keys()
                for key in keys:
                    keySet.add(key)
        return list(keySet)
    
    def values(self):
        valueSet = set()
        for element in self.keyMap:
            if element is None: continue     
            for eachElement in element:
                values = eachElement.values()
                for value in values:
                    valueSet.add(value)
        return list(valueSet)
        
          
            

ht = HashTable()
ht.set("Mike", 21)
ht.set("Alison", 24)
ht.set("omega", 22)
ht.set("tesla", 30)
ht.set("nin", 5)
print(ht.values())
print(ht.keys())
        
        
        
