#Hashing
print("Welcome")
print("/n Type here what u want: ")
n=list(map(int,input().split()))
freq={}
for x in n:
    if x in freq:
        freq[x]+=1
    else:
        freq[x]=1
print(freq)


# 380. Insert Delete GetRandom O(1)
class RandomizedSet:
    def __init__(self):
        self.n = set()

    def insert(self, val: int) -> bool:
        if val in self.n:
            return False
        else:
            self.n.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.n:
            self.n.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.n))




