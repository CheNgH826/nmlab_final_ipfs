from ipfs import Miner

# HOST = '10.37.10.214'
HOST = '0.0.0.0'
PORT = 12345
ipfs_id = '/ip4/10.37.10.214/tcp/4001/ipfs/QmZg8RFQz3zLt4GAKCYfxpWdgw2e4NZnHgYDxYzGMMAtmx'

myMiner = Miner(HOST, PORT, ipfs_id)
myMiner.listen()
