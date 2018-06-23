from ipfs import Owner

HOST1 = '140.112.21.80'     # speech
HOST2 = '140.112.245.175'   # dorm
HOST3 = '52.229.62.3'       # azure vm
PORT = 12345

myOwner = Owner(HOST1, PORT)
# '''
print(myOwner.minerList)
myOwner.add_file('foo')
print(myOwner.minerList)
# '''
# myOwner.get_file('QmYTGM4Kz2kGVMCPSpTK2NHe8TKe8kH7aB7WZYxjDYpoUW', 'foo')
