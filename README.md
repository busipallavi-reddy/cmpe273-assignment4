# cmpe273-assignment4

## Part I. HRW Hashing

Implemented Rendezvous hashing to shard the data as:

* Created a separate cache_client_hrw.py for HRW hashing.
* Instead of getting node from the earlier node ring, implemented get_hrw_node() in client side.
* This function gets the highest node weight for a given key from all the nodes and the key is then sent to that particular node.
* To run HRW hasing, run **python3 cache_client_hrw.py**

*Output*

```
pallavi@desktop:~/Desktop/cmpe273/assignments/cmpe273-assignment4$ python3 cache_client_hrw.py
Nodes and Weights [('127.0.0.1', 4000, 9), ('127.0.0.1', 4001, 6), ('127.0.0.1', 4002, 10), ('127.0.0.1', 4003, 27)]
Connecting to server at 127.0.0.1:4003
b'd0df71363130955e493c24ac0d296a75'
Nodes and Weights [('127.0.0.1', 4000, 27), ('127.0.0.1', 4001, 10), ('127.0.0.1', 4002, 4), ('127.0.0.1', 4003, 14)]
Connecting to server at 127.0.0.1:4000
b'1c84c3d6dec3775654c4573ca4df1064'
Nodes and Weights [('127.0.0.1', 4000, 16), ('127.0.0.1', 4001, 13), ('127.0.0.1', 4002, 21), ('127.0.0.1', 4003, 16)]
Connecting to server at 127.0.0.1:4002
b'e52f43cd2c23bb2e6296153748382764'
Nodes and Weights [('127.0.0.1', 4000, 2), ('127.0.0.1', 4001, 12), ('127.0.0.1', 4002, 2), ('127.0.0.1', 4003, 7)]
Connecting to server at 127.0.0.1:4001
b'9aa0c932fb8eba9a72a6ae60064a0507'
Nodes and Weights [('127.0.0.1', 4000, 3), ('127.0.0.1', 4001, 26), ('127.0.0.1', 4002, 12), ('127.0.0.1', 4003, 25)]
Connecting to server at 127.0.0.1:4001
b'6aaae4a8f8468ef61e78b4ced80fa140'
Nodes and Weights [('127.0.0.1', 4000, 9), ('127.0.0.1', 4001, 6), ('127.0.0.1', 4002, 10), ('127.0.0.1', 4003, 27)]
Connecting to server at 127.0.0.1:4003
b'd0df71363130955e493c24ac0d296a75'
Number of Users=6
Number of Users Cached=5
d0df71363130955e493c24ac0d296a75
Nodes and Weights [('127.0.0.1', 4000, 9), ('127.0.0.1', 4001, 6), ('127.0.0.1', 4002, 10), ('127.0.0.1', 4003, 27)]
Connecting to server at 127.0.0.1:4003
b'{"name": "John Smith", "email": "jsmith@gmail.com", "age": 20}'
9aa0c932fb8eba9a72a6ae60064a0507
Nodes and Weights [('127.0.0.1', 4000, 2), ('127.0.0.1', 4001, 12), ('127.0.0.1', 4002, 2), ('127.0.0.1', 4003, 7)]
Connecting to server at 127.0.0.1:4001
b'{"name": "Agueda Letsinger", "email": "aletsinger@gmail.com", "age": 23}'
e52f43cd2c23bb2e6296153748382764
Nodes and Weights [('127.0.0.1', 4000, 16), ('127.0.0.1', 4001, 13), ('127.0.0.1', 4002, 21), ('127.0.0.1', 4003, 16)]
Connecting to server at 127.0.0.1:4002
b'{"name": "Irish Rackers", "email": "irackers@gmail.com", "age": 22}'
1c84c3d6dec3775654c4573ca4df1064
Nodes and Weights [('127.0.0.1', 4000, 27), ('127.0.0.1', 4001, 10), ('127.0.0.1', 4002, 4), ('127.0.0.1', 4003, 14)]
Connecting to server at 127.0.0.1:4000
b'{"name": "Bari Pushard", "email": "bpushard@gmail.com", "age": 21}'
6aaae4a8f8468ef61e78b4ced80fa140
Nodes and Weights [('127.0.0.1', 4000, 3), ('127.0.0.1', 4001, 26), ('127.0.0.1', 4002, 12), ('127.0.0.1', 4003, 25)]
Connecting to server at 127.0.0.1:4001
b'{"name": "Lisbeth Stacker", "email": "lstacker@gmail.com", "age": 24}'
```



## Part II. Consistent Hashing

#### Features: 

##### *1. Add virtual node layer in the consistent hashing.* 

##### *2. Implement virtual node with data replication.*

* Implemented Consistent hashing with replication factor = 2 , 16 Virtual nodes and ring size of 400.
* The replica node for a server will be the next node on the ring.
* While PUTing a key, data is sent to both the servers the master and its replica.
* While GETing a key, data is fetched from the master node.
* Implemented a class called Ch_Ring in ch_node_ring.py file, which on invocation configures the virtual nodes and the replica servers.
* Created a separate client_cache_ch.py for consistent hashing. This client now invokes the Ch_Ring class instead of NodeRing for consistent hashing.

* To run Consistent hasing, run **python3 cache_client_ch.py**
* In the output, first the Ring configuration is printed for vNode to pNode maaping followed by the replica server lists for each node. Then for each key the corresponding vnode and pnodes that key is sent to. Finally, the get for each key from the master node.

*Output*

```
pallavi@desktop:~/Desktop/cmpe273/assignments/cmpe273-assignment4$ python3 cache_client_ch.py
Ring Configuration: vNode, pNode
75 127.0.0.1:4003
80 127.0.0.1:4000
83 127.0.0.1:4001
152 127.0.0.1:4002
154 127.0.0.1:4001
177 127.0.0.1:4000
195 127.0.0.1:4002
215 127.0.0.1:4000
272 127.0.0.1:4000
287 127.0.0.1:4003
294 127.0.0.1:4003
298 127.0.0.1:4001
315 127.0.0.1:4003
318 127.0.0.1:4002
326 127.0.0.1:4002
382 127.0.0.1:4001

Servers, replica servers
127.0.0.1:4000 ['127.0.0.1:4000', '127.0.0.1:4001']
127.0.0.1:4001 ['127.0.0.1:4001', '127.0.0.1:4002']
127.0.0.1:4002 ['127.0.0.1:4002', '127.0.0.1:4003']
127.0.0.1:4003 ['127.0.0.1:4003', '127.0.0.1:4000']

-----------------------------------------------------------------------------------------------------
Key, hashed key address on ring, virtual node addresses on ring 
 d0df71363130955e493c24ac0d296a75 341 [75, 80, 83, 152, 154, 177, 195, 215, 272, 287, 294, 298, 315, 318, 326, 382]
Address selected  382
Connecting to server at 127.0.0.1:4001
Connecting to server at 127.0.0.1:4002
b'd0df71363130955e493c24ac0d296a75'

-----------------------------------------------------------------------------------------------------
Key, hashed key address on ring, virtual node addresses on ring 
 1c84c3d6dec3775654c4573ca4df1064 196 [75, 80, 83, 152, 154, 177, 195, 215, 272, 287, 294, 298, 315, 318, 326, 382]
Address selected  215
Connecting to server at 127.0.0.1:4000
Connecting to server at 127.0.0.1:4001
b'1c84c3d6dec3775654c4573ca4df1064'

-----------------------------------------------------------------------------------------------------
Key, hashed key address on ring, virtual node addresses on ring 
 e52f43cd2c23bb2e6296153748382764 36 [75, 80, 83, 152, 154, 177, 195, 215, 272, 287, 294, 298, 315, 318, 326, 382]
Address selected  75
Connecting to server at 127.0.0.1:4003
Connecting to server at 127.0.0.1:4000
b'e52f43cd2c23bb2e6296153748382764'

-----------------------------------------------------------------------------------------------------
Key, hashed key address on ring, virtual node addresses on ring 
 9aa0c932fb8eba9a72a6ae60064a0507 135 [75, 80, 83, 152, 154, 177, 195, 215, 272, 287, 294, 298, 315, 318, 326, 382]
Address selected  152
Connecting to server at 127.0.0.1:4002
Connecting to server at 127.0.0.1:4003
b'9aa0c932fb8eba9a72a6ae60064a0507'

-----------------------------------------------------------------------------------------------------
Key, hashed key address on ring, virtual node addresses on ring 
 6aaae4a8f8468ef61e78b4ced80fa140 80 [75, 80, 83, 152, 154, 177, 195, 215, 272, 287, 294, 298, 315, 318, 326, 382]
Address selected  80
Connecting to server at 127.0.0.1:4000
Connecting to server at 127.0.0.1:4001
b'6aaae4a8f8468ef61e78b4ced80fa140'

-----------------------------------------------------------------------------------------------------
Key, hashed key address on ring, virtual node addresses on ring 
 d0df71363130955e493c24ac0d296a75 341 [75, 80, 83, 152, 154, 177, 195, 215, 272, 287, 294, 298, 315, 318, 326, 382]
Address selected  382
Connecting to server at 127.0.0.1:4001
Connecting to server at 127.0.0.1:4002
b'd0df71363130955e493c24ac0d296a75'
Number of Users=6
Number of Users Cached=5
6aaae4a8f8468ef61e78b4ced80fa140

-----------------------------------------------------------------------------------------------------
Key, hashed key address on ring, virtual node addresses on ring 
 6aaae4a8f8468ef61e78b4ced80fa140 80 [75, 80, 83, 152, 154, 177, 195, 215, 272, 287, 294, 298, 315, 318, 326, 382]
Address selected  80
Connecting to server at 127.0.0.1:4000
b'{"name": "Lisbeth Stacker", "email": "lstacker@gmail.com", "age": 24}'
d0df71363130955e493c24ac0d296a75

-----------------------------------------------------------------------------------------------------
Key, hashed key address on ring, virtual node addresses on ring 
 d0df71363130955e493c24ac0d296a75 341 [75, 80, 83, 152, 154, 177, 195, 215, 272, 287, 294, 298, 315, 318, 326, 382]
Address selected  382
Connecting to server at 127.0.0.1:4001
b'{"name": "John Smith", "email": "jsmith@gmail.com", "age": 20}'
1c84c3d6dec3775654c4573ca4df1064

-----------------------------------------------------------------------------------------------------
Key, hashed key address on ring, virtual node addresses on ring 
 1c84c3d6dec3775654c4573ca4df1064 196 [75, 80, 83, 152, 154, 177, 195, 215, 272, 287, 294, 298, 315, 318, 326, 382]
Address selected  215
Connecting to server at 127.0.0.1:4000
b'{"name": "Bari Pushard", "email": "bpushard@gmail.com", "age": 21}'
e52f43cd2c23bb2e6296153748382764

-----------------------------------------------------------------------------------------------------
Key, hashed key address on ring, virtual node addresses on ring 
 e52f43cd2c23bb2e6296153748382764 36 [75, 80, 83, 152, 154, 177, 195, 215, 272, 287, 294, 298, 315, 318, 326, 382]
Address selected  75
Connecting to server at 127.0.0.1:4003
b'{"name": "Irish Rackers", "email": "irackers@gmail.com", "age": 22}'
9aa0c932fb8eba9a72a6ae60064a0507

-----------------------------------------------------------------------------------------------------
Key, hashed key address on ring, virtual node addresses on ring 
 9aa0c932fb8eba9a72a6ae60064a0507 135 [75, 80, 83, 152, 154, 177, 195, 215, 272, 287, 294, 298, 315, 318, 326, 382]
Address selected  152
Connecting to server at 127.0.0.1:4002
b'{"name": "Agueda Letsinger", "email": "aletsinger@gmail.com", "age": 23}'
```

