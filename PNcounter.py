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



