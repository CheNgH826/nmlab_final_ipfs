import socket
import os
import _thread as thread

class Owner():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.minerList = []

    def add_file(self, filename):
        add_log = os.popen('ipfs add %s' %filename).read()
        print(add_log)
        hash_value = add_log.split()[1]
        self.request_pin(hash_value)
    
    def get_file(self, hash_value, filename):
        os.system('ipfs get %s -o %s'%(hash_value, filename))
    
    def request_pin(self, hash_value):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.host, self.port))
        client.send(hash_value.encode())
        data = client.recv(1024)
        self.add_miner(data.decode())
    
    def add_miner(self, miner_ipfs_id):
        self.minerList.append(miner_ipfs_id)

    def check_file(self, file, token):
        pass
        #    for miner in self.minerList:


class Miner():
    def __init__(self, host, port, ipfs_id):
        self.host = host
        self.port = port
        self.ipfs_id = ipfs_id

    def pin_file(self, hash_value):
        os.system('ipfs pin add %s'%hash_value)

    def listen(self):
        serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serv.bind((self.host, self.port))
        serv.listen(5)
        while True:
            (csock, adr) = serv.accept()
    
            data = csock.recv(1024)
            hash_value = data.decode()
            self.pin_file(hash_value)
            csock.send(self.ipfs_id.encode())

if __name__ == '__main__':
    pass
