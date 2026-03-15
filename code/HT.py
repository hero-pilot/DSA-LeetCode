class HashTable:
    def __init__(self, size= 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash+ ord(letter) *23) % len(self.data_map)
        return my_hash
    
    def print_hashtable(self):
        for i, value in enumerate(self.data_map):
            print(i ,":" ,value)
    
    def set(self, key, value):
        index = self.__hash(key) 
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for item in self.data_map[index]:
                if item[0] == key:
                    return item[1]
        return None
    
    def keys(self):
        keys =[]
        for i in range(len(self.data_map)):
            if self.data_map[i] is None: 
                continue  
            for item in self.data_map[i]:
                keys.append(item[0])
        return keys

mytable = HashTable()
mytable.set("bolts", 700)
mytable.set("wahsers", 1000)
mytable.set("Ic'c", 800)
mytable.set("kals", 500)
print(mytable.keys())
