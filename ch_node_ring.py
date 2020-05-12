from pickle_hash import hash_code_hex, deserialize
import bisect

class Ch_Ring():

    def __init__(self, nodes):

        self.rf = 2 # Replication Factor: 2
        self.vrf = 4 # Mapping of number of vnodes to 1 physical node
        self.node_count = len(nodes) # Number of physical nodes
        self.vnodes = self.node_count * self.vrf # Number of Virtual Nodes: 16
        self.nodes = nodes # Actual physical nodes
        self.ring_size = self.node_count * 100 # Ring Size
        self.replicas = dict() # replica dictionary

        # Replication Assignment
        for i in range(self.node_count):
            self.replicas[nodes[i]] = []
            for j in range(self.rf):
                self.replicas[nodes[i]].append(nodes[(i+j) % len(nodes)])

        # Obtain ring virtual addresses and their corresponding nodes (vnode addr, actual node)
        self.ring = []
        for node in nodes:
            for i in range(self.vrf):
                ring_addr = int(hash_code_hex((str(node.port) + str(i)).encode()), 16) % self.ring_size
                self.ring.append((ring_addr, node))

        # print(self.ring)
        # Sort the ring virual addresses
        self.ring.sort(key=lambda x: x[0])

        print("Ring Configuration: vNode, pNode")
        for a, b in self.ring:
            print(a, b.host + ":" + str(b.port))

        print("\nServers, replica servers")
        for node in self.replicas:
            print(node.host + ":" + str(node.port), [b.host + ":" + str(b.port) for b in self.replicas[node]])


    # Get node for a key
    def __get_node(self, key):
        print("\n-----------------------------------------------------------------------------------------------------")
        h = int(key, 16) % self.ring_size
        print("Key, hashed key address on ring, virtual node addresses on ring \n", key, h, [a for a, b in self.ring])
        if h > self.ring[-1][0]:
            vnode = 0
        else:
            vnode_addresses = list(map(lambda x: x[0], self.ring))
            vnode = bisect.bisect_left(vnode_addresses, h)
        print("Address selected ", self.ring[vnode][0])
        return self.ring[vnode][1]


    def send(self, key, databytes):
        operation = deserialize(databytes)['operation']
        if operation == 'PUT':
            nodes = self.replicas[self.__get_node(key)]
            responses = []
            for node in nodes:
                responses.append(node.send(databytes))
            return responses[0]
        else:
            return self.__get_node(key).send(databytes)

