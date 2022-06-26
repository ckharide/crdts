class GSet:

    def __init__(self):
        self.gset = set()

    def addmember(self,item):
        self.gset.add(item)
    
    def merge(self, other):
        self.gset = self.gset.union(other.gset)
    
    def compare(self, other):
        return self.gset.issubset(other.gset)

    def lookup(self,item):
        if item in self.gset:
            print("Item Exists")
            return True
        else:
            print ("Deosnt exist")
            return False
    
    def display(self):
        print(self.gset)

gset1 = GSet()
gset2  = GSet()

gset1.addmember("A")
gset2.addmember("D")
gset1.addmember("C")
gset1.addmember("B")

print(gset1.compare(gset2))
print(gset2.compare(gset1))
print("")
gset2.display()
print("Looking up prior to merge" , gset1.lookup("D"))
print (gset1.merge(gset2))
print("Looking up after merge" , gset1.lookup("D"))
gset1.display()
