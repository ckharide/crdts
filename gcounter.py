class GCounter:

    def __init__(self,n):
        self.count = n
        self.replicas = {}
        print(range(self.count))
        for i in range(self.count):
            self.replicas[i] = 0

    def increment(self,i):
        assert i < self.count
        self.replicas[i] = self.replicas[i] + 1

    def query(self):
        return sum(self.replicas.values())

    
    def compare(self , other):
        for x, y in zip(self.replicas.values , other.replicas.values):
            if( x > y ):
                return False
        return True

    def merge(self , other):
        zips = zip(self.replicas.values() , other.replicas.values())
        for key in self.replicas:
         self.replicas[key] = [max(x, y) for (x, y) in zips]

    def display(self):
        for i in self.replicas :
            print(self.replicas[i])
    

gc1 = GCounter(10)
gc1.increment(4)
gc1.increment(2)
gc1.increment(7)
gc1.increment(4)


gc2 = GCounter(10)
gc2.increment(3)
gc2.increment(4)
gc2.increment(2)
gc2.increment(3)


gc1.merge(gc2)
gc1.display()
