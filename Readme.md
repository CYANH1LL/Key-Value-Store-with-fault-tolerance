# **Building Fault-Tolerant Key-Value Store**


---

Building a distributed Fault-Tolerant Key-Value Store on nodes running membership protocol.

The project was forked from University of Illinois at Urbana-Champaign' [Cloud Computing Specialization](https://www.coursera.org/specializations/cloud-computing) programming assignment.



---
Project Specification
---

The project implements the following functionalities:

1. A key-value store supporting CRUD operations (Create, Read, Update, Delete). 
2. Load-balancing (via a consistent hashing ring to hash both servers and keys).
3. Fault-tolerance up to two failures (by replicating each key three times to three successive nodes in the ring, starting from the first node at or to the clockwise of the hashed key).
4. Quorum consistency level for both reads and writes (at least two replicas).
5. Stabilization after failure (recreate three replicas after failure).

---
Project Architecture
---

Similar to [membership protocol](https://github.com/cyanh1ll/membership-protocol) project, we are running on three-layer framework that will allow to run multiple copies of peers within one process running a single-threaded simulation engine. The three layers are:
1. The lower EmulNet (network)
2. The middle layer including: MP1Node (membership protocol) and the MP2Node (the key-value store)
3. The application layer.

Think of this like a three-layer protocol stack with App, P2P, and EmulNet as the three layers (from top to bottom). Each node in the P2P layer is logically divided in two components: MP1Node and MP2Node. MP1Node runs a membership protocol and MP2Node is implemented to support all the KV Store functionalities. At each node,the key-value store talks to the membership protocol and receives from it the membership list. It then uses this to maintain its view of the virtual ring. Periodically, each node engages in the membership protocol to try to bring its membership list up to date.

<img src="img/key-value.JPG" width="480" alt="Combined Image" />

Please note that the membership list may be stale at nodes! This models the reality in distributed systems.  Also, when reacting to a failure (e.g., by re-replicating a key whose replica failed),there is no contention among the would-be replicas, i.e. no over-replicate keys.

Each MP2Node implements both the client-side as well as the server-side APIs for all the CRUD operations. The application layer chooses a non-faulty node randomly as the client. The same node can be considered as the coordinator. The coordinator is assumed to be never crashed. The Key-Value store accepts std::string as key and value.

---
### Logging

What nodes should log the messages? 
1. All replicas (non-faulty only) should log a success or a fail message for all the CRUD operations AND
2. If the coordinator gets quorum number of successful replies then it should log a successful message, else it should log a failure message

---
Real-world application
---

This is an experimental implementation project that is not ready in production environments.

Here are some ideas to integrate this into real-world application: The MP has been designed for use of porting to a real distributed system. Start by changing the EmulNet layer and then perhaps using multithreading.



---
