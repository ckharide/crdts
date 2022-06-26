# CFRTS
Conflict Free Replicated Data Types

CFRTDS are used where concurrent updates to multiple replicas of the same data are needed, without coordination between the computers hosting the replicas.

# Usage
Conflict-free Replicated Data Types (CRDTs) are used in systems with optimistic replication, where they take care of conflict resolution. 
CRDTs ensure that, no matter what data modifications are made on different replicas, the data can always be merged into a consistent state. 
This merge is performed automatically by the CRDT, without requiring any special conflict resolution code or user intervention.

# Examples

## Growth Only Counter 
## PN Counter
## G-Only Set

# References 

https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type
https://hal.inria.fr/hal-00932836/file/CRDTs_SSS-2011.pdf - Shapiro, Marc; Preguiça, Nuno; Baquero, Carlos; Zawirski, Marek
