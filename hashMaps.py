"""
Hash-map structure with a simple hashing function.
Hash collisions are appended to forma LinkedList.
Worst case search will be O(n) when all the elements
collide to form one single linked list.
Disadvantage: Uses a lot of memory. Memory intensive.
"""
class Hashmap:
    def __init__(self):
        self.length = 0
        self.maxLen = 100
        self.arr = [[] for i in range(self.maxLen)]

    def hashFunc(self, key):
        keyStr = str(key)
        hash = 0
        for i in keyStr:
            hash += ord(i)
        return hash % self.maxLen

    def __setitem__(self, key, value):
        hashVal = self.hashFunc(key)

        if not self.arr[hashVal]:
            self.arr[hashVal] = [(key, value)]
        else:
            self.arr[hashVal].append((key, value))

    def __getitem__(self, key):
        hashVal = self.hashFunc(key)
        if type(self.arr[hashVal]) is list:
            for ele in self.arr[hashVal]:
                if ele[0] == key:
                    return ele[1]
        else:
            return self.arr[hashVal][0][1]

    def print(self):
        counter = 0;
        for ele in self.arr:
            if ele:
                print(f"{counter}, {ele}")
            counter+=1



if __name__ == '__main__':
    hmap = Hashmap()
    hmap["apple10"] = 10
    hmap["apple01"] = 100
    hmap["apple20"] = 20
    hmap["banana"] = 8
    hmap["mango"] = 15
    hmap["pineapple"] = 12

    print(hmap["mango"])
    print(hmap["apple01"])

    hmap.print()