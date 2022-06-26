class GCounter:

    def __init__(self,n):
        self.count = n
        self.replicas = {}

    def increment(self,i):
        assert i <= self.count
        if i not in self.replicas:
         self.replicas[i] = 0 
        self.replicas[i] += 1 
        

    def query(self):
        return sum(self.replicas.values())

    
    def compare(self , other):
        for x, y in zip(self.replicas.values , other.replicas.values):
            if( x > y ):
                return False
        return True

    def merge(self , other):
        merged = dict(self.replicas)
        if len(merged) > 0 :
            for key in other.replicas:
                if key not in merged or other.replicas[key] > merged[key]:
                    merged[key] = other.replicas[key]
            self.replicas = merged
        

    def display(self):
        print(self.replicas)
    


