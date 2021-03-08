import socket


hostname = socket.gethostname()
print(hostname)
host = socket.gethostbyname(hostname)
print(host)
print(socket.gethostbyname('localhost'))
