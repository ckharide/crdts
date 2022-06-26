class PSet:

    def __init__(self):
        self.pset = set()
        self.aset = set()
    
    def add(self, member):
        self.pset.add(member)

    def remove(self, member):
        if (self.lookup(member)):
            self.aset.add(member)
    
    def lookup(self, member):
        b = (member in self.pset and member not in self.aset)
        print(b)
        return b
    
    def compare(self, other):
        return self.gset.issubset(other.gset) & self.aset.issubset(other.aset)
    
    def merge(self, other):
        self.pset = self.pset.union(other.pset)
        self.aset = self.aset.union(other.aset)

    def display(self):
        print(self.pset)
        print(self.aset)

pset1 = PSet()
pset1.add("A")
pset1.add("B")
pset1.remove("A")
pset1.add("A")
pset1.display()