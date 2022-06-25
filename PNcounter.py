from gcounter import GCounter

class PNCounter:

    def __init__(self, n):
        self.pcounter = GCounter(n)
        self.ncounter = GCounter(n)
        self.value = 0

    def increment(self,i):
        self.pcounter.increment(i)

    def decrement(self,i):
        self.ncounter.increment(i)

    def merge(self, other):
        self.pcounter.merge(other.pcounter)
        self.ncounter.merge(other.ncounter)

    def query(self):
        return (self.pcounter.query() - self.ncounter.query())
    
    def display(self):
        print("Increment")
        self.pcounter.display()
        print("Decrement")
        self.ncounter.display()


p1 = PNCounter(3)
p2 = PNCounter(3)
p1.increment(1)
p1.increment(2)
p1.query()

p2.increment(3)

p1.display()
p2.display()
p1.merge(p2)
p1.display()
print(p1.query())
