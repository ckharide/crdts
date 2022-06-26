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


