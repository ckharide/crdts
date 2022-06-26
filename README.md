# CFRTS
Conflict Free Replicated Data Types

CFRTDS are used where concurrent updates to multiple replicas of the same data are needed, without coordination between the computers hosting the replicas.

# Usage
Conflict-free Replicated Data Types (CRDTs) are used in systems with optimistic replication, where they take care of conflict resolution. 
CRDTs ensure that, no matter what data modifications are made on different replicas, the data can always be merged into a consistent state. 
This merge is performed automatically by the CRDT, without requiring any special conflict resolution code or user intervention.

# Examples

## Growth Only Counter 
```
gc1 = GCounter(10)
''' add to the 4th , 2nd and 7 replica '''
gc1.increment(4) 
gc1.increment(2)
gc1.increment(7)
gc1.increment(4)

''' Returns 4 and displays the state of the counter '''
gc1.display()
print(gc1.query())
gc1.merge(gc2)
print(gc1.query())
```

## PN Counter
```
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

```
## G-Only Set

# References 

- https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type
- https://hal.inria.fr/hal-00932836/file/CRDTs_SSS-2011.pdf - Shapiro, Marc; Preguiça, Nuno; Baquero, Carlos; Zawirski, Marek
