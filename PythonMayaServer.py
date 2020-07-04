# PythonServer.py
import socket
import json

# For test the server
def getipaddrs(hostname):
    result = socket.getaddrinfo(hostname, None, 0, socket.SOCK_STREAM)
    return [x[4][0] for x in result]

# Maya Render Server
host = ''
hostname = socket.gethostname()
hostip = getipaddrs(hostname)
print('host name:', hostname)
print('host ip:', hostip)

# Local Maya Application Socket
localHostIp = '127.0.0.1'
localPort = 54321
localAddr = (localHostIp, localPort)

# define the port
# Arbitrary non-privileged port
port = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()

# Debug information
print('socket is Listening')

while True:
    print('Connected by', addr)
    data = conn.recv(1024)

    if not data:
        break
    text = json.loads(data.decode('utf-8'))
    print('ReceivedText', text)
    # print('json:showType:', text["showType"])

    if text["showType"] == 0 :

        print('Maya Client Start')
        mayaClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mayaClient.connect(localAddr)

        # In This Place you can send the Message you want
        # the command from external editor to maya
        cmd = 'mc.polyCube();'

        # Remember to use the encode() function to translate the information
        MyMessage = 'python("import maya.cmds as mc;{0}")'.format(cmd).encode('utf-8')
        mayaClient.send(MyMessage)

        # receive the result info
        data = mayaClient.recv(1024)
        mayaClient.close()
        print('Maya Client Close')
        print('The Result is %s' % data)

    # Send back the original data
    # conn.sendall(data)
    print('ReceivedData', repr(data))


conn.close()
print('the Ending of server')
