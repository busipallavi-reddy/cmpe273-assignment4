import struct
import sys
import socket

from sample_data import USERS
from server_config import NODES
from pickle_hash import serialize_GET, serialize_PUT
# from node_ring import NodeRing

BUFFER_SIZE = 1024

class UDPClient():
    def __init__(self, host, port):
        self.host = host
        self.port = int(port)       

    def send(self, request):
        print('Connecting to server at {}:{}'.format(self.host, self.port))
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(request, (self.host, self.port))
            response, ip = s.recvfrom(BUFFER_SIZE)
            return response
        except socket.error:
            print("Error! {}".format(socket.error))
            exit()

def iptoint(ip):
    ip = socket.inet_aton(ip)
    return struct.unpack("!L", ip)[0]

def weight(key, node):
    a = 1103515245
    b = 12345
    return (a * ((a * node + b) ^ int(key, 16)) + b) % (2 ^ 31)

def get_hrw_node(key, udp_clients):
    wts = []
    for node in udp_clients:
        # print(iptoint(str(node.host)))
        wt = weight(key, iptoint(str(node.host)) * (2 ** 16) + node.port)
        wts.append((node, wt))
    print("Nodes and Weights", [ (n.host, n.port, w) for n, w in wts])
    max_w = wts[0][1]
    max_n = wts[0][0]
    for n, w in wts:
        if w > max_w:
            max_n = n
            max_w = w
    return max_n


def process(udp_clients):
    # client_ring = NodeRing(udp_clients)
    hash_codes = set()
    # PUT all users.
    for u in USERS:
        data_bytes, key = serialize_PUT(u)
        #call RHW
        node = get_hrw_node(key, udp_clients)
        # response = client_ring.get_node(key).send(data_bytes)
        response = node.send(data_bytes)
        print(response)
        hash_codes.add(str(response.decode()))


    print(f"Number of Users={len(USERS)}\nNumber of Users Cached={len(hash_codes)}")
    
    # GET all users.
    for hc in hash_codes:
        print(hc)
        data_bytes, key = serialize_GET(hc)
        # call RHW
        node = get_hrw_node(key, udp_clients)
        response = node.send(data_bytes)
        # response = client_ring.get_node(key).send(data_bytes)
        print(response)


if __name__ == "__main__":
    clients = [
        UDPClient(server['host'], server['port'])
        for server in NODES
    ]
    process(clients)
